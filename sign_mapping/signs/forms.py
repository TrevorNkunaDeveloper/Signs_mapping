from django import forms
from .models import Sign

class SignForm(forms.ModelForm):
    latitude = forms.DecimalField(max_digits=9, decimal_places=6)
    longitude = forms.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        model = Sign
        fields = ['name', 'image', 'latitude', 'longitude']
