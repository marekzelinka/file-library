import pytest

from main import Library


@pytest.fixture
def library():
    return Library()


@pytest.fixture
def library_with_books(library):
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    return library


def test_add_book(library) -> None:
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    assert library.books == [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
    ]


def test_get_book(library) -> None:
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    assert library.get_book(0) == "Title: The Great Gatsby, Author: F. Scott Fitzgerald"


def test_update_book(library_with_books) -> None:
    library_with_books.update_book(0, "The Catcher in the Rye", "J.D. Salinger")

    assert library_with_books.books[0] == {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
    }


def test_list_books(library_with_books) -> None:
    assert library_with_books.list_books() == (
        "Title: To Kill a Mockingbird, Author: Harper Lee\n"
        "Title: 1984, Author: George Orwell"
    )
