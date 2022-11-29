from audioop import add
from django.urls import path
from . views import home,add_new_event
urlpatterns = [
    path("", home,name='home'),
    path("category/<str:category>/",home,name="home-category"),
    path("new/",add_new_event,name="new")
]
