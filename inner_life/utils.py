import locale
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from departments.models import Employee
from .models import Event


class EventCalendar(HTMLCalendar):
	def __init__(self, year=None, month=None, day=None):
		locale.setlocale(locale.LC_TIME, 'ru') 
		self.year = year
		self.month = month
		self.day = day
		super(EventCalendar, self).__init__()

	def formatday(self, day, events):
		events_per_day = events.filter(date__day=day)

		month = list(self.itermonthdays3(self.year, self.month))[-1][2]
		year = list(self.itermonthdays3(self.year, self.month))[-1][0]

		data = ''
		
		if year == datetime.now().year:
			for event in events_per_day:
				data += f'<li>{event.name}</li>'

		if day == datetime.now().day and month == datetime.now().month and year == datetime.now().year:
			return f'<td class="today"><span class="date"><b>{day}</b> <i class="bx bxs-pin"></i></span><ul> {data} </ul></td>'
		elif day == self.day:
			return f'<td class="marked"><span class="date">{day}</span> <span class="text-danger"><i class="bx bxs-down-arrow"></i></span><ul> {data} </ul></td>'
		elif day != 0:
			if len(data) > 0:
				return f'<td class="marked-event"><span class="date">{day}</span><ul> {data} </ul></td>'
			return f'<td class="existing-days"><span class="date">{day}</span><ul> {data} </ul></td>'

		return '<td></td>'

	def formatweek(self, theweek, events):
		week = ''
		for day, weekday in theweek:
			week += self.formatday(day, events)
		return f'<tr> {week} </tr>'

	def formatmonth(self, withyear=True):
		events = Event.objects.filter(date__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
