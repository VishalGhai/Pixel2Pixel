from django import forms
from .models import Image

class ImageView(forms.ModelForm):
    class Meta:
        model = Image
        fields =[
            'image',
            'w',
            'h',
        ]
        