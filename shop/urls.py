from .views import pizza_list, pizza_details
from django.urls import path

urlpatterns = [
    path('pizza/', pizza_list),
    path('pizza/<int:pk>', pizza_details),
]
