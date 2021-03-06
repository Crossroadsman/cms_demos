# Details of 11.1 from Custom User Model Implementation
# (see users.models for full outline)
#
# - create SignUp view GCBV

from django.urls import reverse_lazy
from django.views import generic

from users.forms import WagtailUserCreationForm


class SignUp(generic.CreateView):
    form_class = WagtailUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
