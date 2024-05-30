from django.forms import ModelForm
from django import forms
from .models import Locations, Incident, FireStation

class Loc_Form(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"

class Incident_Form(ModelForm):
    datetime = forms.DateField(
        label="Incident Date",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    class Meta:
        model = Incident
        fields = "__all__"


class FireStationzForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"
