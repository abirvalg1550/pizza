from .views import pizza_list
from django.urls import path

urlpatterns = [
    path('pizza/', pizza_list)
]
