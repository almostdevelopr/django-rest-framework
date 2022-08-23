from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import LoginSerializer, PersonSerializer

from rest_framework.views import APIView

from rest_framework import viewsets

# Create your views here.


@api_view(['GET', 'POST', 'PUT'])
def index(request):
    """A function that returns some data after validating the
    request method from the front end user.
    """
    courses = {
        'course_name': 'Python',
        'learn': ['flask', 'Django', 'FastApi', 'Tornado'],
        'course_provide': 'Youtube'
    }
    if request.method == 'GET':
        print(request.GET.get('search'))  # to get search keyword
        print('You hit a GET method.')
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print('******')
        print(data['name'])
        print('******')
        print('You hit a POST method.')
        return Response(courses)
    elif request.method == 'PUT':
        print('You hit a PUT method.')
        return Response(courses)


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({"message": "sucess"})

    return Response(serializer.errors)


class PersonAPI(APIView):
    """An APIView view class to handle all the requests methods."""

    def get(self, request):
        persons = Person.objects.filter(color__isnull=False)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
        # return Response({"message": "This is get request."})

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)

        # check if data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({"message": "This is post request."})

    def put(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({"message": "This is put request."})

    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({"message": "This is patch request."})

    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"message": "Person deleted"})
        # return Response({"message": "This is delete request."})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    """A simple attempt to serialize the person model's data."""
    if request.method == 'GET':
        persons = Person.objects.filter(color__isnull=False)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = PersonSerializer(data=data)

        # check if data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "PUT":
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    data = request.data
    obj = Person.objects.get(id=data['id'])
    obj.delete()
    return Response({"message": "Person deleted"})


class PersonViewSet(viewsets.ModelViewSet):
    """
    A ViewSet class is simply a type of class-based View, that does not provide any method
    handlers such as .get() or .post(), and instead provides actions such as .list() and .create().
    The method handlers for a ViewSet are only bound to the corresponding actions at the point of
    finalizing the view, using the .as_view() method.


    Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll
    register the viewset with a router class, that automatically determines the urlconf for you.
    """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        """Modifying deafault search functionality."""

        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)

        serializer = PersonSerializer(queryset, many=True)
        return Response({"status": 200, "data": serializer.data})
