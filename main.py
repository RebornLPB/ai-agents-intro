import asyncio
import sys
from google.adk.runners import InMemoryRunner
from google.genai import types
from agents.explainer_agent import explainer_agent
from agents.practice_designer_agent import practice_designer_agent
from agents.reviewer_agent import reviewer_agent
from tools.file_writer import save_markdown_file
from tools.validation import validate_required_sections
from tools.checks import check_environment


async def run_agent(agent, prompt: str) -> str:
    runner = InMemoryRunner(agent=agent, app_name="study_guide")
    session = await runner.session_service.create_session(app_name="study_guide", user_id="user")
    message = types.Content(
        role="user",
        parts=[types.Part(text=prompt)],
    )
    text = ""
    async for event in runner.run_async(user_id="user", session_id=session.id, new_message=message):
        if event.is_final_response() and event.content and event.content.parts:
            text = event.content.parts[0].text
    return text


def assemble_markdown(topic: str, explanation: str, practice: str) -> str:
    return (
        f"# Topic\n\n{topic}\n\n"
        f"{explanation}\n\n"
        f"## Practice Exercise\n\n{practice}"
    )


def assemble_final_markdown(draft: str, review: str) -> str:
    return f"{draft}\n\n## Review Comments\n\n{review}"


async def run_study_guide(topic: str):
    if not topic.strip():
        raise ValueError("Topic cannot be empty.")
    print(f"Topic: {topic}")

    print("1/4 Explaining...")
    explanation = await run_agent(explainer_agent, f"Explain the following topic: {topic}")

    print("2/4 Designing practice...")
    practice = await run_agent(
        practice_designer_agent,
        f"Topic: {topic}\n\nExplanation:\n{explanation}",
    )

    draft = assemble_markdown(topic, explanation, practice)

    print("3/4 Reviewing...")
    review = await run_agent(reviewer_agent, f"Review this draft study guide:\n\n{draft}")

    final_markdown = assemble_final_markdown(draft, review)

    print("4/4 Validating and saving...")
    result = validate_required_sections(final_markdown)
    if result["is_valid"]:
        print("Validation OK")
    else:
        print(f"Warning: missing sections: {result['missing_sections']}")

    file_name = topic.lower().replace(" ", "_")
    print(save_markdown_file(f"output/{file_name}.md", final_markdown))


async def main():
    check_environment()
    if len(sys.argv) > 1:
        await run_study_guide(" ".join(sys.argv[1:]))
    else:
        await run_study_guide("Python decorators")
        await run_study_guide("HTTP status codes")


if __name__ == "__main__":
    asyncio.run(main())
