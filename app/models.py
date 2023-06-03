from django.db import models

# Create your models here.
from django.urls import reverse

from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE ,related_name='question')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

