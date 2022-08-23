from django.urls import path, include
from home.views import PersonAPI, PersonViewSet, index, login, person


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PersonViewSet, basename='people')
urlpatterns = router.urls

# abc.com/api/index

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('persons/', PersonAPI.as_view()),
    # path('', include(router.urls))
]
