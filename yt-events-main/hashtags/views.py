from django.shortcuts import render, get_object_or_404
from .models import Hashtag
from events.models import Event

# Create your views here.


def home(request, hashtag):
    hashtag = get_object_or_404(Hashtag, title=hashtag)
    events = Event.objects.filter()
    return render(request, 'hashtags/home.html', {'hashtag':hashtag})