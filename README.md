# Blog Generator API

A FastAPI service that generates a blog from a topic, optionally in a requested language.

## Requirements

- Python 3.14 or newer
- An OpenAI API key
- A LangSmith API key, read from `LANGCHAIN_API_KEY` by the current app startup code

## Install and configure

From the project root, create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your-openai-api-key
LANGCHAIN_API_KEY=your-langsmith-api-key
```

Keep `.env` private and do not commit API keys.

## Run the API

With the virtual environment active and `.env` configured, run:

```bash
PYTHONPATH=src python -m uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is at `http://127.0.0.1:8000/docs`.

## Call it from Postman

1. Start the API using the command above and leave that terminal running.
2. In Postman, create a `POST` request to `http://127.0.0.1:8000/blogs`.
3. Under **Headers**, set `Content-Type` to `application/json`.
4. Under **Body**, select **raw** and choose **JSON**, then send one of these bodies.

Generate a blog about a topic:

```json
{
	"topic": "Agentic AI"
}
```

Generate a blog in a language (for example, Hindi):

```json
{
	"topic": "Agentic AI",
	"language": "hindi"
}
```

The response contains the generated graph state under the `data` property. The `topic` field is required; `language` is optional. The API key belongs in the local `.env` file, not in the Postman request.

## Switch to the language feature branch

The language feature branch is named `feature/with_language`. Switch to it from the project root with:

```bash
git switch feature/with_language
```
