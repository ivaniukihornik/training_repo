class Book:
    def __init__(self, title: str, author: str, year: int, genre: str, copies: int):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.initial_copies = copies
        self.actual_copies = self.initial_copies

    def is_available(self) -> bool:
        return True if self.actual_copies > 0 else False

    def rent(self) -> str:
        if self.is_available():
            self.actual_copies -= 1
            return f'Book is rented. Actual count of copies: {self.actual_copies}'
        else:
            raise ValueError('No available copies')

    def return_book(self) -> str:
        if self.actual_copies + 1 > self.initial_copies:
            raise ValueError('This is not our book')
        self.actual_copies += 1
        return f'Book is returned. Actual count of copies: {self.actual_copies}'


