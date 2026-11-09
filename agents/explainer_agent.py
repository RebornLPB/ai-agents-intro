import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

EXPLAINER_SECTIONS = [
    "Simple Explanation",
    "Key Concepts",
    "Example",
    "Common Mistakes",
    "Final Summary",
]

sections = ""
for s in EXPLAINER_SECTIONS:
    sections = sections + "## " + s + "\n"

load_dotenv()

model_name = os.getenv("MODEL_NAME", "ollama_chat/llama3.1:8b")

instruction = (
    "You are an expert technical instructor, your goal is to explain programming "
    "clearly to students.\n\n"
    "You MUST format your response in Markdown using EXACTLY these headings, "
    "in this order:\n\n"
    + sections
    + "\nWrite 1 to 3 short sentences or bullet points under each heading. "
    "For Common Mistakes, list 2 or 3 mistakes beginners make.\n"
    "Output only these sections, nothing else."
    "\nDo not write any exercise."
    "\nYou MUST write all 5 sections, including Final Summary, which is the last one."
)

explainer_agent = Agent(
    name="explainer_agent",
    model=LiteLlm(model=model_name),
    instruction=instruction,
)
