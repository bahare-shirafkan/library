from rest_framework.decorators import api_view
from rest_framework.response import Response
from book.models import Book
from rest_framework import status
from book.serializers import BookSerializer
from book.services import BookService


@api_view(['POST'])
def store(request):
    title = request.POST['title']
    authors = request.data.getlist('authors[]')
    cities = request.data.getlist('cities[]')
    genres = request.data.getlist('genres[]')
    published_date = request.POST['published_date']
    shabak = request.POST['shabak']
    price = request.POST['price']
    try:
        book_service = BookService()
        book = book_service.createBook(
            title, authors, cities, genres, published_date, shabak, price)

        serializer = BookSerializer(book)
        return Response({'data': serializer.data, 'status': status.HTTP_201_CREATED})
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAll(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({'data': serializer.data})


@api_view(['GET'])
def detail(request, id):
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response({'data': serializer.data})
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update(request, id):
    title = request.POST['title']
    authors = request.data.getlist('authors[]')
    cities = request.data.getlist('cities[]')
    genres = request.data.getlist('genres[]')
    published_date = request.POST['published_date']
    shabak = request.POST['shabak']
    price = request.POST['price']
    try:
        book_service = BookService()
        book = book_service.update(
            id, title, authors, cities, genres, published_date, shabak, price)
        serializer = BookSerializer(book)
        return Response({'data': serializer.data, 'status': status.HTTP_200_OK})
    except ValueError as e:
        return Response({'error': str(e), 'status': status.HTTP_400_BAD_REQUEST})


@api_view(['DELETE'])
def delete(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
