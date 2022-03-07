from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Vacancy, Dismissal


class VacanciesListView(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = 'for_bosses/vacancies.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context['object_list'] = object_list

        return context


class VacancyDetailView(LoginRequiredMixin, DetailView):
    model = Vacancy
    template_name = 'for_bosses/vacancy_detail.html'


class DismissalListView(LoginRequiredMixin, ListView):
    model = Dismissal
    template_name = 'for_bosses/dismissals.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context['object_list'] = object_list

        return context
