from book.models import Book


class BookRepository:
    def create(self, title, authors, cities, genres, published_date, shabak, price):
        book = Book(title=title, published_date=published_date,
                    shabak=shabak, price=price)
        book.save()
        book.authors.set(authors)
        book.genres.set(cities)
        book.cities.set(genres)
        return book

    def getById(book_id):
        try:
            book = Book.objects.get(id=book_id)
            return book
        except Book.DoesNotExist:
            raise Exception("Book not found")

    def update(id, title,authors, cities, genres,  published_date, shabak, price):
        book = Book.objects.get(id=id)
        book.title = title
        book.authors = authors
        book.cities = cities
        book.genres = genres
        book.published_date = published_date
        book.shabak = shabak
        book.price = price
        book.save()
        return book

