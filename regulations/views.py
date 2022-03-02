from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Reglament, Penalty, Bonus


class ReglamentDetailView(LoginRequiredMixin, DetailView):
    model = Reglament
    template_name = 'detailview_template.html'


class PenaltyDetailView(LoginRequiredMixin, DetailView):
    model = Penalty
    template_name = 'detailview_template.html'


class BonusDetailView(LoginRequiredMixin, DetailView):
    model = Bonus
    template_name = 'detailview_template.html'
