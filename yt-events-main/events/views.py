from django.shortcuts import redirect, render
from . models import Event
import datetime
from . forms import EventForm
from hashtags.models import Hashtag
# Create your views here.

def home(request,category = None):
    upcoming_events = Event.objects.all().filter(scheduled_on__gte = datetime.date.today()).order_by('scheduled_on')[:2]
    past_events = Event.objects.all().filter(scheduled_on__lte = datetime.date.today(), is_active = True).order_by('scheduled_on')
    if category is not None:
        past_events = Event.objects.all().filter(scheduled_on__lte = datetime.date.today(), is_active = True,category=category).order_by('-scheduled_on')
    context = {
        "upcoming_events":upcoming_events,
        "past_events":past_events
    }
    return render(request, 'index.html',context)

def add_new_event(request):
    form = EventForm()
    if request.method == "POST":
        new_tags = request.POST["new_tags"]
        tags = new_tags.split(',')
        for tag in tags:
            if not Hashtag.objects.filter(title=tag):
                Hashtag.objects.create(title=tag)
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        "form":form
    }
    return render(request, 'add_event.html',context)