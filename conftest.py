from collections.abc import Generator

import pytest

from main import Library


@pytest.fixture
def library() -> Generator[Library]:
    library = Library()
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    yield library

    library.clear_books()
