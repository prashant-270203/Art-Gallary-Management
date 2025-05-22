from django import forms
from .models import Artist  # Assuming you have an Artist model

class ArtistRegistrationForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio']  # Adjust fields as necessary