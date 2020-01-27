# Details of 4.4 from Custom User Model Implementation
# (see users.models for full outline)
#
# We need to do this because Admin is highly coupled to the default User model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import KSUserChangeForm, KSUserCreationForm
from users.models import KSUser


class KSUserAdmin(UserAdmin):
    add_form = KSUserCreationForm
    form = KSUserChangeForm
    model = KSUser
    list_display = ['username', 'email', 'first_name', 'last_name',]


admin.site.register(KSUser, KSUserAdmin)
