from django import forms

from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo # match Photo table
        fields = '__all__' # use what row