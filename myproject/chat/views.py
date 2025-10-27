from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        rooms = [
            {
                'id': 1,
                'name': 'Общая комната',
                'description': 'Основная комната для общения',
                'participants_count': 15,
                'messages_count': 243
            },
            {
                'id': 2, 
                'name': 'Игровой чат',
                'description': 'Обсуждаем игры и киберспорт',
                'participants_count': 8,
                'messages_count': 89
            }
        ]
        return render(request, 'home.html', {'rooms': rooms})
    else:
        return render(request, 'home.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        
        print(f"Регистрация: {username}")  # Для отладки
        
        # Валидация
        errors = []
        
        if not username:
            errors.append('Имя пользователя обязательно.')
        
        if not password1:
            errors.append('Пароль обязателен.')
        
        if not password2:
            errors.append('Подтверждение пароля обязательно.')
        
        if password1 != password2:
            errors.append('Пароли не совпадают.')
        
        if len(password1) < 3:
            errors.append('Пароль должен содержать минимум 3 символа.')
        
        if User.objects.filter(username=username).exists():
            errors.append('Пользователь с таким именем уже существует.')
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'register.html')
        
        try:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')
    
    # GET запрос
    return render(request, 'register.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        print(f"Вход: {username}")  # Для отладки
        
        if not username or not password:
            messages.error(request, 'Все поля обязательны.')
            return render(request, 'auth.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'С возвращением, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    
    # GET запрос
    return render(request, 'auth.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('home')

@login_required
def room_detail(request, room_id):
    room = {
        'id': room_id,
        'name': 'Общая комната',
        'participants_count': 15,
        'messages_count': 243,
        'links_count': 12,
        'media_count': 8,
        'files_count': 5,
        'music_count': 3,
        'voice_messages_count': 2
    }
    
    messages_list = [
        {
            'user': {'username': 'Администратор', 'is_staff': True},
            'message': 'Добро пожаловать в чат!',
            'timestamp': '19:40'
        },
        {
            'user': {'username': request.user.username, 'is_staff': False},
            'message': 'Привет всем!',
            'timestamp': '19:41'
        }
    ]
    
    context = {
        'room': room,
        'messages': messages_list,
        'participants_count': room['participants_count'],
        'messages_count': room['messages_count'],
        'links_count': room['links_count'],
        'media_count': room['media_count'],
        'files_count': room['files_count'],
        'music_count': room['music_count'],
        'voice_messages_count': room['voice_messages_count']
    }
    return render(request, 'room_detail.html', context)

@login_required
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            messages.success(request, f'Комната "{name}" создана!')
            return redirect('home')
        else:
            messages.error(request, 'Введите название комнаты')
    
    return render(request, 'create_room.html')
