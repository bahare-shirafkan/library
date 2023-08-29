from django_elasticsearch_dsl import Document, fields
from elasticsearch_dsl import Keyword, Text
from book.models import Book

class BookDocument(Document):
    title = fields.TextField()
    author = fields.KeywordField()

    class Index:
        name = 'books'

# Index the data
def index_books():
    books = Book.objects.all()
    for book in books:
        BookDocument(title=book.title, author=book.author).save()