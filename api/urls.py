from django.urls import path
from api import views

urlpatterns = [
    path("" , views.RoomView.as_view() , name="Room")
]
