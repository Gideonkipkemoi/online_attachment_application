from django import forms
from django.forms import ModelForm

from .models import Post

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class StartDateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['position', 'company', 'description', 'start_date']
        widgets = {
            'start_date':DateInput()
        }
