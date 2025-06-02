from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Habit
from .forms import SignUpForm, HabitForm

# Landing page view
def landing_page(request):
    return render(request, 'tracker/landing.html')

# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'tracker/signup.html', {'form': form})


from django.utils import timezone

from django.contrib import messages  # to use Django’s messages framework

@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    today = timezone.now().date()

    if request.method == 'POST':
        for habit in habits:
            checkbox = f'completed_{habit.id}'
            is_checked = checkbox in request.POST

            # Update only if last_updated is not today, or allow toggling if you want
            if habit.last_updated != today or True:  # Remove condition if you want toggling every time
                if is_checked:
                    habit.streak += 1
                    habit.completed_today = True
                else:
                    habit.streak = 0
                    habit.completed_today = False
                habit.last_updated = today
                habit.save()

        return redirect('habit_list')

    total_habits = habits.count()
    longest_streak = max([habit.streak for habit in habits], default=0)
    completed_today = habits.filter(completed_today=True).count()

    return render(request, 'tracker/habit_list.html', {
        'habits': habits,
        'today': today,
        'total_habits': total_habits,
        'longest_streak': longest_streak,
        'completed_today': completed_today,
    })


    

# Add habit (protected, requires login)

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    return render(request, 'tracker/add_habit.html', {'form': form})

