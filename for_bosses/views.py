from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Vacancy, Dismissal


class VacanciesListView(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = 'for_bosses/vacancies.html'


class VacancyDetailView(LoginRequiredMixin, DetailView):
    model = Vacancy
    template_name = 'for_bosses/vacancy_detail.html'


class DismissalListView(LoginRequiredMixin, ListView):
    model = Dismissal
    template_name = 'for_bosses/dismissals.html'
