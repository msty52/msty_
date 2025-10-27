from django.contrib import admin
from .models import ChatRoom, ChatMessage, UserProfile, RoomMember

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'created_at']
    search_fields = ['user__username']

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at', 'is_private']
    list_filter = ['is_private', 'created_at']
    search_fields = ['name']

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'timestamp', 'is_read']
    list_filter = ['room', 'timestamp']
    search_fields = ['message']

@admin.register(RoomMember)
class RoomMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'joined_at', 'is_admin']
    list_filter = ['room', 'is_admin']