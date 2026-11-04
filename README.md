# Setup - Local Model Environment with Ollama & LiteLLM

This project sets up a local agent environment using Google ADK, LiteLLM, and Ollama.

## Prerequisites
- Python 3.10+
- Ollama installed on your machine

## Installation Steps

### 1. Create and activate a Python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install the required Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Install and run Ollama
Download and install Ollama from ollama.com. Then pull the model used for the project:
```bash
ollama pull llama3.1:8b
```

### 4. Configure the environment
Copy the .env.example file to .env:
```bash
cp .env.example .env
```

## Model Used
- **Model**: `llama3.1:8b` (via Ollama)

## Author
- **Dylan** - *Holberton School*
