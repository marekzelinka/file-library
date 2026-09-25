# file-library

Using Pytest Fixtures to test a simple book library.

This project is a lightweight, strictly-typed Python application that implements a basic in-memory `Library` system. It demonstrates modern Python development practices, including the use of `TypedDict`, advanced linting with Ruff, and testing with Pytest fixtures and generators.

## Features

* **Add Books:** Easily add books with a title and author to the library.

* **Update & Retrieve:** Fetch or update book details using their index.

* **List Books:** View all books currently in the library.

* **Clear Library:** Empty the library completely.

* **Testing:** Robust testing setup using Pytest fixtures with setup/teardown yields.

* **Type Safety:** Built with strict type hinting (`mypy`/`pyright` friendly) for Python 3.14+.

## Requirements

* **Python:** `>= 3.14`
* **Package Manager:** [`uv`](https://github.com/astral-sh/uv)

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/marekzelinka/file-library
   cd file-library
   ```

2. **Sync dependencies using `uv`:**
   `uv` will automatically create a virtual environment with Python 3.14+ and install all necessary dependencies and development groups.

   ```bash
   uv sync
   ```

## Usage

You can use the `Library` class to manage a collection of books. Run your script using `uv run`:

```bash
uv run python main.py
```

Basic usage example:

```python
from main import Library

# Initialize the library
library = Library()

# Add books
print(library.add_book("1984", "George Orwell"))
print(library.add_book("To Kill a Mockingbird", "Harper Lee"))

# Update a book
print(library.update_book(0, "Nineteen Eighty-Four", "George Orwell"))

# List all books
print(library.list_books())
```

## Testing

This project utilizes `pytest` for testing, specifically highlighting the use of fixtures for clean test setup and teardown.

The testing suite uses a generator-based fixture to pre-populate the library for tests and automatically clear it afterward:

```python
import pytest
from collections.abc import Generator
from main import Library

@pytest.fixture
def library() -> Generator[Library, None, None]:
    # Setup
    # Create a library with some books
    lib = Library()
    lib.add_book("To Kill a Mockingbird", "Harper Lee")
    lib.add_book("1984", "George Orwell")
    
    # Yield to the test
    yield lib
    
    # Teardown
    # Clear all books from the library
    lib.clear_books()
```

To run the tests with `uv`:

```bash
uv run pytest
```

## Development and Linting

This project enforces strict coding standards using **Ruff**. To run the linter:

```bash
uv run ruff check .
```
