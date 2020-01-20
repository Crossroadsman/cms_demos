# Details of 4.3 from Custom User Model Implementation
# (see users.models for full outline)
#
# We're mostly just subclassing existing forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import WagtailUser


class WagtailUserCreationForm(UserCreationForm):

    class Meta:
        model = WagtailUser
        fields = ('username', 'email',)


class WagtailUserChangeForm(UserChangeForm):

    class Meta:
        model = WagtailUser
        fields = ('username', 'email',)
