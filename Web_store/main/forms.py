from django import forms
from .models import Review, Image


class NewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', )

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

