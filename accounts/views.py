from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Account


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Account
    pk_url_kwarg = 'profile_id'
    login_url = '/login/'
    template_name = 'accounts/profile_info.html'
