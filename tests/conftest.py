import pytest
from src.books import Book
from src.libraries import Library


@pytest.fixture(scope='session')
def create_library():
    book1 = Book('Atlant', 'Rend', 1976, 'antiutopic', 100)
    book2 = Book('Gods', 'Bruyan Writer', 1977, 'fairytale', 10)
    book3 = Book('Cars', 'Scott Paper', 1977, 'antiutopic', 2)
    book4 = Book('Animals', 'Lindy Pergament', 2002, 'antiutopic', 14)
    book5 = Book('Dogs', 'Rend', 1976, 'antiutopic', 3)
    library = Library(book1, book2, book3, book4, book5)
    yield library
    print('Tests are over')
