run:
    uv run main.py

test:
    uv run pytest -v

typecheck:
    uv run pyrefly check

lint:
    uv run ruff check --fix

format:
    uv run ruff format
