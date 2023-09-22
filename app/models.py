from django.db import models
from django.utils import timezone

Universities = (
    ("...........","..........."),
    ("moi university","moi university"),
    
)

class Post(models.Model):
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField()
    
    def __str__(self):
        return self.position
class Apply(models.Model):
    name = models.CharField(max_length=50)
    learning_institution = models.CharField(
        max_length=100,
        choices=Universities,
        default="..........."
    )
    applied_position = models.ForeignKey(Post, on_delete=models.CASCADE)
    expected_start_date = models.DateTimeField()
    curriculum_vite = models.FileField(upload_to="cv_uploads")
    recommendation = models.FileField(upload_to="recom_uploads")
    
    def __str__(self):
        return self.name
    
