
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    streak = models.IntegerField(default=0)
    frequency = models.CharField(max_length=20, choices=[('daily', 'Daily'), ('weekly', 'Weekly')])
    created_at = models.DateTimeField(auto_now_add=True)
    completed_today = models.BooleanField(default=False)
    last_updated = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date_completed = models.DateField()

    def __str__(self):
        return f"{self.habit.name} on {self.date_completed}"
