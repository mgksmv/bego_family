from datetime import datetime, timedelta
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gallery, BestEmployee
from departments.models import Employee


class GalleryListView(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = 'inner_life/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery_by_position = Gallery.objects.filter(access=self.request.user.position)
        context['gallery_by_position'] = gallery_by_position
        return context


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery
    template_name = 'inner_life/gallery_detail.html'


class BestEmployeesListView(ListView):
    model = BestEmployee
    template_name = 'inner_life/best_employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees_by_position = BestEmployee.objects.filter(access=self.request.user.position)
        context['employees_by_position'] = employees_by_position
        return context

    
class EmployeeBirthdays(ListView):
    model = Employee
    template_name = 'inner_life/employee_birthdays.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.today()

        context['current_year'] = datetime.now().year
        context['current_month'] = datetime.now().month
        context['today'] = datetime.now().day
        
        context['birthdays_this_month'] = Employee.objects.filter(
            birth_date__month=today.month, birth_date__day__gte=today.day
        ).order_by('birth_date__day')
        context['other_birthdays'] = Employee.objects.filter(
            birth_date__month__gt=today.month,
            birth_date__day__gte=today.day
        ).order_by('birth_date__month')
        print(f'LENLENLENLEN: {len(context["birthdays_this_month"])}')

        return context
