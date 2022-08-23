from django.urls import path
from home.views import PersonAPI, index, login, person

# abc.com/api/index

urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('persons/', PersonAPI.as_view())
]
