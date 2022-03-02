from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import History, Mission, OrgStructure


class HistoryDetailView(LoginRequiredMixin, DetailView):
    model = History
    template_name = 'detailview_template.html'


class MissionDetailView(LoginRequiredMixin, DetailView):
    model = Mission
    template_name = 'detailview_template.html'


class OrgStructureDetailView(LoginRequiredMixin, DetailView):
    model = OrgStructure
    template_name = 'detailview_template.html'
