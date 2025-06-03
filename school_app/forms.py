from django import forms
from .models import *

class ActivityImages(forms.ModelForm):
    class Meta:
        model = activity
        fields = '__all__'