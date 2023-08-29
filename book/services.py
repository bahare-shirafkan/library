from book.repositories import BookRepository


class BookService:
    def __init__(self) -> None:
        self.book_repository = BookRepository()

    def createBook(self, title, authors, cities, genres, published_date, shabak, price):
        if not title:
            raise ValueError('Title is required.')
        if len(title) > 50:
            raise ValueError("Title Should be at most 50 characters long.")
        if shabak and len(shabak) > 20:
            raise ValueError("Shabak Should be at most 20 characters long.")
        if price and int(price) < 0:
            raise ValueError("Price cannot be negative.")
        if not authors or not genres or not cities:
            raise ValueError('At least one author, genre, and city is required.')

        book = self.book_repository.create(
            title, authors, cities, genres, published_date, shabak, price)
        return book

    def update(self, id, title, authors, cities, genres, published_date, shabak, price):
        if not id:
            raise ValueError('Book id is required.')
        if len(shabak) < 13:
            raise ValueError("Shabak should have at least 13 digit")
        book = self.book_repository.update(
            id, title,authors, cities, genres,  published_date, shabak, price)
        return book
