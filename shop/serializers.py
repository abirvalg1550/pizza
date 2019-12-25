from rest_framework.serializers import Serializer, IntegerField


class PizzaSerializer(Serializer):
    id = IntegerField()
