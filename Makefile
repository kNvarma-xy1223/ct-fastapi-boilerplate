install:
	python -m uv sync

run:
	python -m uv run uvicorn app.main:app --reload

lint:
	python -m uv run ruff check .

format:
	python -m uv run ruff format .

test:
	python -m uv run pytest