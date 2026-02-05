def test_add_book(library) -> None:
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    expected_books = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    ]

    assert sorted(library.books, key=lambda book: book["title"]) == sorted(
        expected_books, key=lambda book: book["title"]
    )


def test_get_book(library) -> None:
    library.add_book("The Catcher in the Rye", "J.D. Salinger")

    assert library.get_book(2) == "Title: The Catcher in the Rye, Author: J.D. Salinger"
