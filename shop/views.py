from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view()
def pizza_list(request):
    return Response()
