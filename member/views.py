from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.models import Member
from rest_framework import status
from member.serializers import MemberSerializer
from member.services import MemberService


# def getOTP(request):
    


@api_view(['POST'])
def store(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    membership_type = request.POST['membership_type']
    validity_date = request.POST['validity_date']
    try:
        member_repository = MemberService()
        member = member_repository.create(
            first_name, last_name, membership_type, validity_date)

        serializer = MemberSerializer(member)
        return Response({'data': serializer.data, 'status': status.HTTP_201_CREATED})
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAll(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response({'data': serializer.data})


@api_view(['GET'])
def detail(request, id):
    try:
        member = Member.objects.get(id=id)
        serializer = MemberSerializer(member)
        return Response({'data': serializer.data})
    except Member.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update(request, id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    membership_type = request.POST['membership_type']
    validity_date = request.POST['validity_date']
    try:
        book_service = MemberService()
        book = book_service.update(
            id, first_name, last_name, membership_type, validity_date)
        serializer = MemberSerializer(book)
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
