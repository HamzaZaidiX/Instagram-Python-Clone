from django import forms
from .models import Image

class newPostForm(forms.ModelForm):
   class Meta:
        model = Image
        exclude = ['profile','comments','name']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class ProfileForm(forms.ModelForm):
   class Meta:
        model = Image
        exclude = ['profile']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }
