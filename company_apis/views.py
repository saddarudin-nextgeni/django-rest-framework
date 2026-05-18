from rest_framework.decorators import api_view
from django.http import HttpResponse


@api_view(['GET'])
def home(request):
    return HttpResponse("Welcome to the Company APIs Home Page!")