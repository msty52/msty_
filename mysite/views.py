from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pytz

def home(request):
    return render(request, 'home.html')  # это важно, без ошибок

def get_time(request):
    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(tz).strftime('%H:%M:%S')
    return HttpResponse(current_time)
