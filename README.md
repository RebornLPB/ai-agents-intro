# AI Agents in Python

## Description

A small multi-agent system built with Google ADK, LiteLLM and a local Ollama model.
Given a topic, it generates a beginner study guide in Markdown and saves it in `output/`.

Pipeline:

```text
Topic -> Explainer Agent -> Practice Designer Agent -> Draft
      -> Reviewer Agent -> Final Markdown -> Validation -> Save
```

## Requirements

- Python 3.10+ (developed with Python 3.12 on WSL Ubuntu)
- [Ollama](https://ollama.com) installed and running
- A local model: `llama3.1:8b`
- Python packages (see `requirements.txt`): `google-adk`, `litellm`, `python-dotenv`, `ollama`

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ollama pull llama3.1:8b
cp .env.example .env
```

## Configuration

The project reads its configuration from a `.env` file at the project root (it is ignored by git).
`.env.example` shows the expected content:

```text
OLLAMA_API_BASE=http://localhost:11434
MODEL_NAME=ollama_chat/llama3.1:8b
```

- `MODEL_NAME`: the model used by all agents (required).
- `OLLAMA_API_BASE`: address of the Ollama server.

No API key is needed with a local model.

## How to Run

Make sure Ollama is running and the virtual environment is active.

With a topic:

```bash
python main.py "Python list comprehensions"
```

Without argument, it runs two default topics (`Python decorators` and `HTTP status codes`):

```bash
python main.py
```

## Example Input

```bash
python main.py "Python list comprehensions"
```

## Example Output

Console:

```text
Topic: Python list comprehensions
1/4 Explaining...
2/4 Designing practice...
3/4 Reviewing...
4/4 Validating and saving...
Validation OK
Saved: output/python_list_comprehensions.md
```

File `output/python_list_comprehensions.md` (shortened):

```markdown
# Topic

Python list comprehensions

## Simple Explanation
A list comprehension is a concise way to create a new list from an existing list ...

## Practice Exercise

### Exercise
Create a new list that contains the squares of all even numbers ...

## Review Comments

### Recommendation
Needs revision. The guide lacks a clear explanation of edge cases ...
```

## Project Structure

```text
ai-agents-intro/
├── main.py                       # runs the pipeline
├── agents/
│   ├── explainer_agent.py
│   ├── practice_designer_agent.py
│   └── reviewer_agent.py
├── tools/
│   ├── file_writer.py            # save_markdown_file()
│   ├── validation.py             # validate_required_sections()
│   └── checks.py                 # check_environment()
├── data/
│   └── topic_examples.json       # not used yet
├── output/                       # generated study guides
├── requirements.txt
├── .env.example                  # configuration template
└── README.md
```

## Agents

- **Explainer Agent** (`agents/explainer_agent.py`): explains the topic with five sections: Simple Explanation, Key Concepts, Example, Common Mistakes, Final Summary.
- **Practice Designer Agent** (`agents/practice_designer_agent.py`): receives the topic and the explanation, and creates one small exercise with expected input, expected output and hints. It does not rewrite the explanation.
- **Reviewer Agent** (`agents/reviewer_agent.py`): reads the draft guide and returns missing information, unclear parts, suggestions and a recommendation. It does not rewrite the guide.

## Tools

- **`save_markdown_file(file_path, content)`**: creates the folder if needed, writes the file, and returns the saved path or an error message.
- **`validate_required_sections(markdown)`**: checks that the 8 required headings exist and returns the missing ones.
- **`check_environment()`**: before the agents run, checks that `MODEL_NAME` is set, that Ollama is reachable and that the model is installed.

## Self-Validation Checklist

TODO: tick each item only after testing it, and add the items from your course checklists.

- [x] `tools/file_writer.py` created with `save_markdown_file()`
- [x] `tools/validation.py` created with `validate_required_sections()`
- [x] Explainer, Practice Designer and Reviewer agents created
- [x] `main.py` runs the full pipeline in order
- [x] A Markdown file is generated in `output/`
- [ ] The validator was tested with valid and incomplete Markdown
- [ ] Error cases were tested (Ollama stopped, wrong model name, empty topic)
- [ ] README commands were re-tested from a clean clone

## Reflection

1. **Direct LLM call vs AI agent.** A direct call sends one prompt to a model and gets one answer. An agent wraps a model with a role and instructions, and can be combined with other agents and tools in a workflow, so each step has a clear job and a clear input and output.

2. **Role of each agent.** The Explainer writes the explanation, the Practice Designer creates an exercise from that explanation, and the Reviewer criticizes the draft without rewriting it.

3. **Role of each tool.** Tools are normal Python code, so they behave the same every time. One writes the file, one checks the structure of the Markdown, and one checks the configuration. The model is not involved in these steps.

4. **Most difficult part.** TODO: write your own answer. For example: understanding that an ADK agent does not return text directly but an async generator of events, so it needs a Runner; or making the agent prompts and the validator use the same headings.

5. **Limitation observed with the model.** `llama3.1:8b` is not always consistent. It sometimes skipped the last section (`Final Summary`), wrote an exercise when it was told not to, and the Reviewer sometimes contradicted itself (listing problems but answering "Approved"). Fields like "Expected Output" were sometimes filled with "Not applicable" when an output was expected. Hardware: TODO (CPU/GPU/RAM). A run chains three model calls and can take several minutes.

## Known Limitations

- The model can skip a section or change a heading. The validator only warns, it does not fix the output.
- The validator checks headings, not the quality of the content.
- The Reviewer is a small model: it can approve a weak guide or give vague comments.
- Section order is not the one of the specification: `Common Mistakes` and `Final Summary` come before `Practice Exercise` and `Review Comments`.
- The file name is built from the topic and does not handle special characters such as `/` or `?`.
- Generation time depends on the hardware and can be several minutes.

## Troubleshooting

| Problem | Message | What to check |
|---|---|---|
| Missing env variable | `MODEL_NAME is missing` | Create a `.env` file with `MODEL_NAME=ollama_chat/llama3.1:8b` |
| Ollama not running | `Cannot reach Ollama at http://localhost:11434` | Start it with `ollama serve`, then retry |
| Model not available | `Model '...' is not installed` | Run `ollama pull <model>` and check the name in `.env` |
| Empty topic | `Topic cannot be empty.` | Pass a topic: `python main.py "Python decorators"` |
| File not saved | `Error: could not save ...` | Check permissions on `output/` and the path |
| Missing sections | `Warning: missing sections: [...]` | The model skipped a heading. Run again; the file is still saved |
| `No module named 'google'` | Python import error | Activate the venv: `source venv/bin/activate` |

## Author

- **Dylan** - *Holberton School*
