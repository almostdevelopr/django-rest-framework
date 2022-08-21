from django.urls import path
from home.views import index

# abc.com/api/index

urlpatterns = [
    path('index/', index),
]
