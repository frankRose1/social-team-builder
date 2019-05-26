from django import forms
from . import models


class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.UserProfile
        fields = ['first_name', 'last_name', 'skills', 'avatar']