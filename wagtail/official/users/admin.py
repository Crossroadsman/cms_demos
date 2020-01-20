# Details of 4.4 from Custom User Model Implementation
# (see users.models for full outline)
#
# We need to do this because Admin is highly coupled to the default User model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import WagtailUserChangeForm, WagtailUserCreationForm
from users.models import WagtailUser


class WagtailUserAdmin(UserAdmin):
    add_form = WagtailUserCreationForm
    form = WagtailUserChangeForm
    model = WagtailUser
    list_display = ['username', 'email', 'first_name', 'last_name',]


admin.site.register(WagtailUser, WagtailUserAdmin)
