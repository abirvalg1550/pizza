from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PizzaSerializer
from .models import Pizza

# Create your views here.


@api_view()
def pizza_list(request):
    pizzas = Pizza.objects.all()
    serializer = PizzaSerializer(pizzas, many=True)
    return Response(data=serializer.data)


@api_view()
def pizza_details(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    serializer = PizzaSerializer(pizza)
    return Response(data=serializer.data)
