test:
    uv run pytest

typecheck:
    uv run pyrefly check

lint:
    uv run ruff check --fix

format:
    uv run ruff format
