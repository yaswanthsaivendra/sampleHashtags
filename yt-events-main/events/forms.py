from django import forms
from django import forms
from . models import Event

class EventForm(forms.ModelForm):
    new_tags = forms.CharField(label="Add new tags seperated by commas",max_length=2000)
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "scheduled_on":forms.DateInput(
                attrs= {
                    "class": "form-control ",
                     "type":'datetime-local'
                }
            )
        }