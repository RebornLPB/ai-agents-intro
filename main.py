import asyncio
import sys
from google.adk.runners import InMemoryRunner
from google.genai import types
from agents.explainer_agent import explainer_agent
from agents.practice_designer_agent import practice_designer_agent
from agents.reviewer_agent import reviewer_agent
from tools.file_writer import save_markdown_file
from tools.validation import validate_required_sections

async def run_explainer(topic: str):
    print(f"Explaining Topic: {topic}")
    prompt = f"Explain the following topic: {topic}"
    runner = InMemoryRunner(agent=explainer_agent, app_name="explainer")
    session = await runner.session_service.create_session(app_name="explainer", user_id="user")
    message = types.Content(
        role="user",
        parts=[types.Part(text=prompt)],
    )
    text= ""
    async for event in runner.run_async(user_id="user", session_id=session.id, new_message=message):
        if event.is_final_response() and event.content and event.content.parts:
            text = event.content.parts[0].text
            print(text)

    result = validate_required_sections(text)
    if not result["is_valid"]:
        print(f"Warning: missing sections: {result['missing_sections']}")

    # --- Practice Designer ---
    print(f"Designing practice for: {topic}")
    practice_prompt = f"Topic: {topic}\n\nExplanation:\n{text}"
    practice_runner = InMemoryRunner(agent=practice_designer_agent, app_name="practice_designer")
    practice_session = await practice_runner.session_service.create_session(app_name="practice_designer", user_id="user")
    practice_message = types.Content(
        role="user",
        parts=[types.Part(text=practice_prompt)],
    )
    practice = ""
    async for event in practice_runner.run_async(user_id="user", session_id=practice_session.id, new_message=practice_message):
        if event.is_final_response() and event.content and event.content.parts:
            practice = event.content.parts[0].text
            print(practice)

    # --- Reviewer ---
    print(f"Reviewing guide for: {topic}")
    draft = text + "\n\n" + practice
    review_runner = InMemoryRunner(agent=reviewer_agent, app_name="reviewer")
    review_session = await review_runner.session_service.create_session(app_name="reviewer", user_id="user")
    review_message = types.Content(
        role="user",
        parts=[types.Part(text=f"Review this draft study guide:\n\n{draft}")],
    )
    review = ""
    async for event in review_runner.run_async(user_id="user", session_id=review_session.id, new_message=review_message):
        if event.is_final_response() and event.content and event.content.parts:
            review = event.content.parts[0].text
            print(review)


    file_name = topic.lower().replace(" ", "_")
    print(save_markdown_file(f"output/{file_name}.md", text + "\n\n" + practice))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(run_explainer(" ".join(sys.argv[1:])))
    else:
        asyncio.run(run_explainer("Python decorators"))
        asyncio.run(run_explainer("HTTP status codes"))
