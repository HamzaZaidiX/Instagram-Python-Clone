from django import forms
from .models import Image

class newPostForm(forms.Form):
   class Meta:
        model = Image
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
