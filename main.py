import asyncio
import sys
from google.adk.runners import InMemoryRunner
from google.genai import types
from agents.explainer_agent import explainer_agent
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

    file_name = topic.lower().replace(" ", "_")
    print(save_markdown_file(f"output/{file_name}.md", text))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(run_explainer(" ".join(sys.argv[1:])))
    else:
        asyncio.run(run_explainer("Python decorators"))
        asyncio.run(run_explainer("HTTP status codes"))
