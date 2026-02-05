from typing import TypedDict


class Book(TypedDict):
    title: str
    author: str


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, title: str, author: str) -> str:
        self.books.append({"title": title, "author": author})

        return "Book added successfully"

    def get_book(self, index: int) -> str:
        if 0 <= index < len(self.books):
            book = self.books[index]
            return f"Title: {book['title']}, Author: {book['author']}"
        else:
            return "Index out of range"

    def update_book(self, index: int, title: str, author: str) -> str:
        if 0 <= index < len(self.books):
            self.books[index]["title"] = title
            self.books[index]["author"] = author
            return "Book updated sucessfully"
        else:
            return "Index out of range"

    def list_books(self) -> str:
        if not self.books:
            return "No books in the library"
        return "\n".join(
            f"Title: {book['title']}, Author: {book['author']}" for book in self.books
        )

    def clear_books(self) -> None:
        self.books = []


def main() -> None:
    library = Library()
    print(library.add_book("1984", "George Orwell"))
    print(library.add_book("To Kill a Mockingbird", "Harper Lee"))
    print(library.update_book(0, "Nineteen Eighty-Four", "George Orwell"))
    print(library.list_books())


if __name__ == "__main__":
    main()
