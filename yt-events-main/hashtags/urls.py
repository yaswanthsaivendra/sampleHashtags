from django.urls import path
from . views import home

app_name = 'hashtags'

urlpatterns = [
    path("<str:hashtag>/", home,name='home'),
]