from django.db import models
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):

    name = models.CharField(max_length=100)
    is_student = models.BooleanField(default=False)
    description = models.TextField()


    def __str__(self):
        return self.name
    
