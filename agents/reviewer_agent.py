import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

model_name = os.getenv("MODEL_NAME", "ollama_chat/llama3.1:8b")

reviewer_agent = Agent(
    name="reviewer_agent",
    model=LiteLlm(model=model_name),
    instruction="""
    You are a reviewer agent.
    Review the draft study guide for clarity, completeness, and usefulness.
    Identify missing or unclear parts. Be specific.
    Provide short, actionable suggestions.
    Do not rewrite the entire guide.

    Format your response in Markdown with these parts:
    ### Missing Information
    ### Unclear Parts
    ### Suggestions
    ### Recommendation
    (Approved or Needs revision, with a short reason)
    If you listed any missing or unclear parts, the recommendation must be "Needs revision".
    Use "Approved" only if both lists are "None".
    """,
)
