import sys
from agents.explainer_agent import explainer_agent

def run_explainer(topic: str):
    print(f"Explaining Topic:")
    prompt = f"Explain the following topic: {topic}"

    response = explainer_agent.run(prompt)
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_explainer(" ".join(sys.argv[1:]))
    else:
        run_explainer("Python decorators")
        run_explainer("HTTP status codes")
