from django.contrib import admin
from .models import Hashtag, Profile, Feedback 
# Register your models here.


class HashtagAdmin(admin.ModelAdmin):
    list_display=('title','is_active')
    list_editable=('is_active',)

admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Profile)
admin.site.register(Feedback)


