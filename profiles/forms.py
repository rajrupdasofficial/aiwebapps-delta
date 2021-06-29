from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    model=Profile
    exclude=('user',)