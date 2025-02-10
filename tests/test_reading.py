import copy

from src.books import Book


def test_book_adding_to_library(create_library):
    library = copy.deepcopy(create_library)
    book = Book('God', 'Gosling', 1978, 'fairytale', 10)
    result = library.add_book(book)
    assert result == 'Book is successfully added to library'
    assert book in library.books


def test_positive_rent_book(create_library):
    library = copy.deepcopy(create_library)
    title = 'Cars'
    book = library.search_by_title(title)
    result = library.rent_book(title)
    assert result == f'Book is rented. Actual count of copies: {book.actual_copies}'


def test_negative_rent_book(create_library):
    library = copy.deepcopy(create_library)
    title = 'Aniimals'
    result = library.rent_book(title)
    assert result == 'No book by specified title'


def test_negative_book_adding(create_library):
    library = copy.deepcopy(create_library)
    book = library.books[2]
    try:
        library.add_book(book)
    except ValueError as error:
        assert str(error) == 'Book is already in library'
    else:
        assert False
