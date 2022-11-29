from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Hashtag(models.Model):
    title = models.CharField("hashtag name", max_length=100)
    is_active = models.BooleanField(default=False)


    def __str__(self) :
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hashtags_followed = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.hashtags_followed.all()}"


class Feedback(models.Model):
    FEEDBACK_CHOICES = (
        ('IP', "Intellectual Property Violation"),
        ('VODO', "Violence or Dangerous organizations"),
        ('BOH', "Bullying or Harassment"),
    )
    text = models.CharField(max_length=200, choices=FEEDBACK_CHOICES)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.hashtag.title} - {self.text} "



    
