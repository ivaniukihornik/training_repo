from src.books import Book


class Library:
    def __init__(self, *books: Book):
        self.books: list = list(books)

    def add_book(self, book: Book) -> str:
        if book in self.books:
            raise ValueError('Book is already in library')
        self.books.append(book)
        return 'Book is successfully added to library'

    def search_by_author(self, author: str) -> Book | str:
        book = list(filter(lambda book: book.author == author, self.books))
        return book[0] if len(book) else 'No book written by specified author'

    def search_by_genre(self, genre: str) -> Book | str:
        book = list(filter(lambda book: book.genre == genre, self.books))
        return book[0] if len(book) else 'No book by specified genre'

    def search_by_title(self, title: str) -> Book | str:
        book = list(filter(lambda book: book.title == title, self.books))
        return book[0] if len(book) else 'No book by specified title'

    def rent_book(self, title: str) -> str:
        search_result = self.search_by_title(title)
        if isinstance(search_result, Book):
            return search_result.rent()
        else:
            return search_result

    def return_book(self, title: str) -> str:
        search_result = self.search_by_title(title)
        if search_result is Book:
            return search_result.return_book()
        else:
            return search_result
