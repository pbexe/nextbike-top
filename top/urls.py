from django.urls import include, path
from .views import home, bike

urlpatterns = [
    path("", home),
    path("bike/<int:number>", bike)
]