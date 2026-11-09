import json
import os
import urllib.error
import urllib.request

from dotenv import load_dotenv


def check_environment():
    load_dotenv()

    model = os.getenv("MODEL_NAME")
    if not model:
        raise ValueError(
            "MODEL_NAME is missing. Add it to your .env file, "
            "for example: MODEL_NAME=ollama_chat/llama3.1:8b"
        )

    base_url = os.getenv("OLLAMA_API_BASE", "http://localhost:11434")
    try:
        with urllib.request.urlopen(base_url + "/api/tags", timeout=5) as response:
            installed = [m["name"] for m in json.load(response)["models"]]
    except (urllib.error.URLError, OSError) as e:
        raise ConnectionError(
            f"Cannot reach Ollama at {base_url}. Is it running? Try: ollama serve"
        ) from e

    name = model.split("/", 1)[-1]
    if name not in installed and name + ":latest" not in installed:
        raise ValueError(
            f"Model '{name}' is not installed. Run: ollama pull {name}\n"
            f"Installed models: {installed}"
        )
