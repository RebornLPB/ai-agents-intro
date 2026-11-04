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

## Example output
Explaining Topic: HTTP status codes
## HTTP Status Codes: Understanding Web Response Messages
HTTP status codes are three-digit numbers returned by a web server in response to a client's request. These codes indicate the result of the request, such as successful delivery, errors, or redirections.

### Key Concepts
- **200 OK**: Request was successful, and the requested resource is returned.
- **404 Not Found**: Requested resource could not be found on the server.
- **500 Internal Server Error**: Server encountered an unexpected condition that prevented it from fulfilling the request.

### Simple Example
Suppose you visit a website (http://example.com) and you enter a URL of a page that doesn't exist, let's say http://example.com/non-existent-page. In this case, the server will return a 404 status code, indicating that the requested page does not exist on the server. This status code is an HTTP status code example, where the server is clearly indicating that the page cannot be found.

### Practical Application
Understanding HTTP status codes is crucial for both web developers and end-users. Developers need to handle different status codes in their application to improve user experience.For instance, if a request returns a 404 status code, the application can display a friendly error message to the user, instead of a generic error page.

## Author
- **Dylan** - *Holberton School*
