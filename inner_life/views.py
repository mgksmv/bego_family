import calendar
from datetime import datetime, timedelta

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe

from .models import Gallery, BestEmployee, Event
from .forms import DateForm
from .utils import EventCalendar
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


class EventCalendarView(ListView):
    model = Event
    template_name = 'inner_life/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_date = get_date(self.request.GET.get('date', None))

        cal = EventCalendar(current_date.year, current_date.month, current_date.day)

        html_cal = cal.formatmonth(withyear=True)

        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(current_date)
        context['next_month'] = next_month(current_date)
        context['form'] = DateForm()

        return context


def get_date(req_day):
    if req_day:
        try:
            year, month, day = (int(x) for x in req_day.split('-'))
            return datetime(year, month, day)
        except ValueError:
            year, month = (int(x) for x in req_day.split('-'))
            return datetime(year, month, day=1)
    return datetime.today()


def prev_month(current_date):
    first = current_date.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'date=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(current_date):
    days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
    last = current_date.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'date=' + str(next_month.year) + '-' + str(next_month.month)
    return month
