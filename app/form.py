from django import forms
from django.forms import ModelForm

from .models import Post, Apply

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class StartDateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['position', 'company', 'description', 'start_date', 'apply_before']
        widgets = {
            'start_date':DateInput(),
            'apply_before':DateInput()
        }
class ApplyStartDateForm(ModelForm):
    class Meta:
        model = Apply
        fields = ['name','learning_institution', 'applied_position',
                'expected_start_date', 'curriculum_vite', 'recommendation'
]
        widgets = {
            'expected_start_date':DateInput()
        }
