import pytest

from main import Library


@pytest.fixture
def library():
    library = Library()
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    yield library

    library.clear_books()
