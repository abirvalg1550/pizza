from rest_framework.viewsets import ModelViewSet
from .serializers import PizzaSerializer
from .models import Pizza

# Create your views here.


class PizzaViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
