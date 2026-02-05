class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

        return "Book added successfully"

    def get_book(self, index):
        if 0 <= index < len(self.books):
            book = self.books[index]
            return f"Title: {book['title']}, Author: {book['author']}"
        else:
            return "Index out of range"

    def update_book(self, index, title, author):
        if 0 <= index < len(self.books):
            self.books[index]["title"] = title
            self.books[index]["author"] = author
            return "Book updated sucessfully"
        else:
            return "Index out of range"

    def list_books(self):
        if not self.books:
            return "No books in the library"
        return "\n".join(
            f"Title: {book['title']}, Author: {book['author']}" for book in self.books
        )

    def clear_books(self):
        self.books = []


def main():
    library = Library()
    print(library.add_book("1984", "George Orwell"))
    print(library.add_book("To Kill a Mockingbird", "Harper Lee"))
    print(library.update_book(0, "Nineteen Eighty-Four", "George Orwell"))
    print(library.list_books())


if __name__ == "__main__":
    main()
