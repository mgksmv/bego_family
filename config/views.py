from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import calendar, locale
from calendar import HTMLCalendar

from regulations.models import Reglament


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


@login_required
def search(request):
    reglaments = None

    if 'keyword' in request.GET:
        query = request.GET.get('keyword')
        if query:
            reglaments = Reglament.objects.filter(name__icontains=query)

    return render(request, 'search.html', {'reglaments': reglaments})


@login_required
def calendar_view(request, year, month):
    month = month.capitalize()
    print(list(calendar.month_name))
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

    # cal = HTMLCalendar().formatmonth(year, month_number)

    class CustomHTMLCal(calendar.HTMLCalendar):
        cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun text-danger"]
        cssclass_month_head = "text-center month-head"
        cssclass_month = "text-center month"
        cssclass_year = "text-italic lead"

        def formatday(self, day, events):
            events_per_day = events.filter(start_time__day=day)
            d = ""
            for event in events_per_day:
                d += f"<li> {event.get_html_url} </li>"
            if day != 0:
                return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
            return "<td></td>"

    cal = CustomHTMLCal().formatmonth(year, month_number)

    return render(request, 'calendar.html', {'cal': cal})
