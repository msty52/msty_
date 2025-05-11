from django.shortcuts import render
from django.http import JsonResponse
import pytz
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def get_time(request):
    tz = pytz.timezone('Europe/Moscow')
    now = datetime.now(tz)
    current_time = now.strftime('%H:%M:%S')
    current_date = now.strftime('%d.%m.%Y')
    return JsonResponse({'time': current_time, 'date': current_date})
