from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learn': ['flask', 'Django', 'FastApi', 'Tornado'],
        'course_provide': 'Youtube'
    }
    if request.method == 'GET':
        print('You hit a GET method.')
        return Response(courses)
    elif request.method == 'POST':
        print('You hit a POST method.')
        return Response(courses)
    elif request.method == 'PUT':
        print('You hit a PUT method.')
        return Response(courses)
