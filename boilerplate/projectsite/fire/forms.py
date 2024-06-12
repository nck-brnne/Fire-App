from django.forms import ModelForm
from django import forms
from .models import Locations, Incident, FireStation, WeatherConditions, FireTruck

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

class Weather_condition(ModelForm):
    class Meta:
        model = WeatherConditions
        fields = "__all__"
        
        
class Firetruckform(ModelForm):
    class Meta: 
        model = FireTruck
        fields = "__all__" 