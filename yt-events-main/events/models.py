from django.db import models
from hashtags.models import Hashtag

# Create your models here.

class Event(models.Model):
    category_choices = (
        ('tech-talks','Tech Talks'),
        ('freelancing','Freelancing'),
        ('content-creation','Content Creations'),
        ('finance','Finance'),
        ('entrepreneurship','Entrepreneurship'),
     
    )
    title = models.CharField(max_length = 255)
    video_id =models.CharField( max_length=50)
    thumbnail = models.ImageField(upload_to = "thumbnail/%Y/%m/")
    is_active = models.BooleanField(default = True)
    category = models.CharField(max_length=100,choices=category_choices)
    scheduled_on = models.DateTimeField()
    
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    
    def __str__(self):
        return f'{self.title} - {self.scheduled_on}'