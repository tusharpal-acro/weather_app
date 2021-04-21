from django import forms

class WeatherForm(forms.Form):
    longitude = forms.CharField(label='longitude', max_length=20)
    latitude = forms.CharField(label='latitude', max_length=20)
