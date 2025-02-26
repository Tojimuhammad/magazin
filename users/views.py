from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import User

@api_view(['POST'])
def sign_up(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        User.objects.create_user(username=username, password=password)
        return Response({'message':'Success'})
    except:
        return Response(f'{username} username is busy')
   
    
@api_view(['POST'])
def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    usr = authenticate(username=username, password=password)
    if usr:
        login(request, usr)
        return Response(f'{username} successfully logged in')
    else:
        return Response('Error username or password')
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def log_out(request):
    logout(request)
    return Response('logged out')