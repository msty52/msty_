from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    path('create-room/', views.create_room, name='create_room'),
]
