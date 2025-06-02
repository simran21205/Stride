
from django.contrib import admin
from .models import Habit, HabitCompletion

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'frequency', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('frequency', 'created_at')
    ordering = ('-created_at',)

@admin.register(HabitCompletion)
class HabitCompletionAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date_completed')
    search_fields = ('habit__name',)
    list_filter = ('date_completed',)
    ordering = ('-date_completed',)
