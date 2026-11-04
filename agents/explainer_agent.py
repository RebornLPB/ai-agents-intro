import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

model_name = os.getenv("MODEL_NAME", "ollama_chat/llama3.1:8b")

explainer_agent = Agent(
    name="explainer_agent",
    model=LiteLlm(model=model_name),
    instructions="""
    You are an expert technical instructor, your goal is to explain programming
    clearly to students.

    You MUST format your response in Markdown with the following structure:

    ##Short Explanation
    A clear and simple explanation (2 to 4 sentences max)

    ### Key Concepts
    - Concept 1: brief explanation
    - Concept 2: brief explanation
    - Concept 3: brief explanation

    ### Simple Example
    A short, concrete code or real-world example.
    """
)
