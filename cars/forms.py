from django import forms
from .models import *


class UsersForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = [""]  #поля , которые необходимо исключить