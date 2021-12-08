from django.shortcuts import render
from rest_framework.generics import CreateAPIView , ListAPIView , UpdateAPIView 
from api.models import Room
from api.serializers import RoomSerializer

# Create your views here.
class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

