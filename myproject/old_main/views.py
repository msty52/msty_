from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Message
from .serializers import UserSerializer, MessageSerializer

# API Views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# Template View
def home(request):
    return render(request, 'main/index.html')