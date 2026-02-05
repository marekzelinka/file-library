from main import Library


def test_update_book(library: Library) -> None:
    library.update_book(0, "The Catcher in the Rye", "J.D. Salinger")

    assert library.books[0] == {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
    }


def test_list_books(library: Library) -> None:
    assert library.list_books() == (
        "Title: To Kill a Mockingbird, Author: Harper Lee\n"
        "Title: 1984, Author: George Orwell"
    )
