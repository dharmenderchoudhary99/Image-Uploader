from django import forms
from .models import Image 

class Image(forms.ModelForm):
    class Meta:
        model = Image
        fields ='__all__'
        labels={'photo':''}