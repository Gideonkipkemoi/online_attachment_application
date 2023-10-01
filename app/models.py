from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse
from datetime import timedelta

Universities = (
    ("Moi university","Moi university"),
    ("kenyatta university","Kenyatta university"),
    ("University of Nairobi","University of Nairobi"),
    ("Chuka university","Chuka university"),
    ("Egerton university","Egerton university"),
    ("University of Eldoret","University of Eldoret"),
    
)

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Post(models.Model):
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateField(validators=[validate_date])
    apply_before = models.DateField(validators=[validate_date])
    
    def __str__(self):
        return self.position
    
    def get_absolute_url(self):
        return reverse('home')

def validate_expected_start_date(date):
    if date + timedelta(days=5) < timezone.now().date():
        raise ValidationError("Please apply 5 days from now")  
   
class Apply(models.Model):
    name = models.CharField(max_length=50)
    learning_institution = models.CharField(
        max_length=100,
        choices=Universities
    )
    applied_position = models.ForeignKey(Post, on_delete=models.CASCADE)
    expected_start_date = models.DateField(validators=[validate_expected_start_date], blank=True, null=True)
    curriculum_vite = models.FileField(upload_to="cv_uploads")
    recommendation = models.FileField(upload_to="recom_uploads")
    application_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.expected_start_date:
            self.expected_start_date=self.applied_position.start_date+timedelta(days=5)
            super().save(*args,**kwargs)

    @property
    def position(self):
        return self.applied_position.position

    
    def __str__(self):
        return f'{self.name} application'
    
    def get_absolute_url(self):
        return reverse('home')
    
