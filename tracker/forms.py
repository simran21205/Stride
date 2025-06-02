from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Habit

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border border-secondary',
                'placeholder': 'Enter task name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light border border-secondary',
                'placeholder': 'Enter description',
                'rows': 3,
            }),
            'frequency': forms.Select(attrs={
                'class': 'form-select bg-dark text-light border border-secondary',
            }),
        }
# class HabitForm(forms.ModelForm):
#     class Meta:
#         model = Habit
#         fields = ['name', 'description', 'frequency']

#     def __init__(self, *args, **kwargs):
#         super(HabitForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
