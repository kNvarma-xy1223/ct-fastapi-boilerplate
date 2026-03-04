# CT FastAPI Boilerplate

## Stack
- FastAPI
- Pydantic
- Uvicorn
- uv (dependency management)
- Ruff (linting)
- pre-commit (code quality hooks)
- Makefile (command abstraction)

## Setup

python -m uv sync

## Run

python -m uv run uvicorn app.main:app --reload

## Docs

Open: http://127.0.0.1:8000/docs

## Run API
uv run uvicorn app.main:app --reload

## Start LM Studio
Start the LM Studio local server at http://127.0.0.1:1234

## Test
Open http://127.0.0.1:8000/docs and use POST /chat

