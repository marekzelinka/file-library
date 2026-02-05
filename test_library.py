from main import Library


def test_add_book() -> None:
    library = Library()
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    assert library.books == [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
    ]


def test_get_book() -> None:
    library = Library()
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    assert library.get_book(0) == "Title: The Great Gatsby, Author: F. Scott Fitzgerald"


def test_update_book() -> None:
    library = Library()
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.update_book(0, "The Catcher in the Rye", "J.D. Salinger")

    assert library.books[0] == {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
    }


def test_list_books() -> None:
    library = Library()
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    assert library.list_books() == (
        "Title: To Kill a Mockingbird, Author: Harper Lee\n"
        "Title: 1984, Author: George Orwell"
    )
