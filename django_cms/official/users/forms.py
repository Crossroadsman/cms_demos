# Details of 4.3 from Custom User Model Implementation
# (see users.models for full outline)
#
# We're mostly just subclassing existing forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import KSUser


class KSUserCreationForm(UserCreationForm):

    class Meta:
        model = KSUser
        fields = ('username', 'email',)


class KSUserChangeForm(UserChangeForm):

    class Meta:
        model = KSUser
        fields = ('username', 'email',)
