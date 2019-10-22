from django import forms
from .models import Image,Profile

class newPostForm(forms.ModelForm):
   class Meta:
        model = Image
        exclude = ['profile','comments','name','user','likes']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class ProfileForm(forms.ModelForm):
   class Meta:
        model = Profile
        exclude = ['user']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }
