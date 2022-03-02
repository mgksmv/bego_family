from django.urls import path

from .views import VacanciesListView, VacancyDetailView, DismissalListView

urlpatterns = [
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('vacancies/<slug:slug>', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('dismissals/', DismissalListView.as_view(), name='dismissals'),
]
