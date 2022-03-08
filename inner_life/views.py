import calendar
from datetime import datetime, timedelta

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Gallery, BestEmployee, Event, RecordBook, Video, Giveaway, Tradition, Nomination
from .forms import DateForm
from .utils import EventCalendar
from departments.models import Employee


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

    
class EmployeeBirthdays(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'inner_life/employee_birthdays.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.today()

        birthdays_this_month = Employee.objects.filter(
            birth_date__month=today.month, birth_date__day__gte=today.day
        ).order_by('birth_date__day')

        other_birthdays = Employee.objects.filter(
            birth_date__month__gt=today.month,
            birth_date__day__gte=today.day
        ).order_by('birth_date__month')
        
        paginator = Paginator(other_birthdays, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            other_birthdays_paginated = paginator.page(page)
        except PageNotAnInteger:
            other_birthdays_paginated = paginator.page(1)
        except EmptyPage:
            other_birthdays_paginated = paginator.page(paginator.num_pages)

        context['current_year'] = datetime.now().year
        context['current_month'] = datetime.now().month
        context['today'] = datetime.now().day
        
        context['birthdays_this_month'] = birthdays_this_month
        context['other_birthdays'] = other_birthdays_paginated

        return context


class EventCalendarView(LoginRequiredMixin, ListView):
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


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'inner_life/event_detail.html'


class RecordBookListView(LoginRequiredMixin, ListView):
    model = RecordBook
    template_name = 'listview_template.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list_paginated = paginator.page(page)
        except PageNotAnInteger:
            object_list_paginated = paginator.page(1)
        except EmptyPage:
            object_list_paginated = paginator.page(paginator.num_pages)

        context['object_list'] = object_list_paginated
        context['model_name'] = self.model._meta.verbose_name_plural
        return context


class RecordBookDetailView(LoginRequiredMixin, DetailView):
    model = RecordBook
    template_name = 'detailview_template.html'


class VideoListView(LoginRequiredMixin, ListView):
    model = Video
    template_name = 'listview_template.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list_paginated = paginator.page(page)
        except PageNotAnInteger:
            object_list_paginated = paginator.page(1)
        except EmptyPage:
            object_list_paginated = paginator.page(paginator.num_pages)

        context['object_list'] = object_list_paginated
        context['model_name'] = self.model._meta.verbose_name_plural
        return context


class VideoDetailView(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'detailview_template.html'


class GiveawaysListView(LoginRequiredMixin, ListView):
    model = Giveaway
    template_name = 'listview_template.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list_paginated = paginator.page(page)
        except PageNotAnInteger:
            object_list_paginated = paginator.page(1)
        except EmptyPage:
            object_list_paginated = paginator.page(paginator.num_pages)

        context['object_list'] = object_list_paginated
        context['model_name'] = self.model._meta.verbose_name_plural
        return context


class GiveawaysDetailView(LoginRequiredMixin, DetailView):
    model = Giveaway
    template_name = 'detailview_template.html'


class TraditionsListView(LoginRequiredMixin, ListView):
    model = Tradition
    template_name = 'listview_template.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list_paginated = paginator.page(page)
        except PageNotAnInteger:
            object_list_paginated = paginator.page(1)
        except EmptyPage:
            object_list_paginated = paginator.page(paginator.num_pages)

        context['object_list'] = object_list_paginated
        context['model_name'] = self.model._meta.verbose_name_plural
        return context


class TraditionsDetailView(LoginRequiredMixin, DetailView):
    model = Tradition
    template_name = 'detailview_template.html'


class NominationsListView(LoginRequiredMixin, ListView):
    model = Nomination
    template_name = 'listview_template.html'
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list_paginated = paginator.page(page)
        except PageNotAnInteger:
            object_list_paginated = paginator.page(1)
        except EmptyPage:
            object_list_paginated = paginator.page(paginator.num_pages)

        context['object_list'] = object_list_paginated
        context['model_name'] = self.model._meta.verbose_name_plural
        return context


class NominationsDetailView(LoginRequiredMixin, DetailView):
    model = Nomination
    template_name = 'detailview_template.html'
