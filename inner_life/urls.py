from django.urls import path

from .views import GalleryListView, GalleryDetailView, BestEmployeesListView, EmployeeBirthdays, EventCalendarView

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/<slug:slug>/', GalleryDetailView.as_view(), name='gallery_detail'),
    path('best-employees/', BestEmployeesListView.as_view(), name='best_employees'),
    path('employee-birthdays/', EmployeeBirthdays.as_view(), name='employee_birthdays'),
    path('event-calendar/', EventCalendarView.as_view(), name='event_calendar'),
]
