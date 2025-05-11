from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_time', views.get_time, name='get_time'),  # <-- ВОТ это добавляем!
]
