from django.urls import path

from .views import (
    GalleryListView,
    GalleryDetailView,
    BestEmployeesListView,
    EmployeeBirthdays,
    EventCalendarView,
    EventDetailView,
    RecordBookListView,
    RecordBookDetailView,
    VideoListView,
    VideoDetailView,
    GiveawaysListView,
    GiveawaysDetailView,
    TraditionsListView,
    TraditionsDetailView,
    NominationsListView,
    NominationsDetailView
)

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/<slug:slug>/', GalleryDetailView.as_view(), name='gallery_detail'),
    path('best-employees/', BestEmployeesListView.as_view(), name='best_employees'),
    path('employee-birthdays/', EmployeeBirthdays.as_view(), name='employee_birthdays'),
    path('event-calendar/', EventCalendarView.as_view(), name='event_calendar'),
    path('event-calendar/<slug:slug>/', EventDetailView.as_view(), name='event_detail'),
    path('record-book/', RecordBookListView.as_view(), name='record_book'),
    path('record-book/<slug:slug>/', RecordBookDetailView.as_view(), name='record_book_detail'),
    path('video/', VideoListView.as_view(), name='video'),
    path('video/<slug:slug>/', VideoDetailView.as_view(), name='video_detail'),
    path('giveaways/', GiveawaysListView.as_view(), name='giveaways'),
    path('giveaways/<slug:slug>/', GiveawaysDetailView.as_view(), name='giveaways_detail'),
    path('traditions/', TraditionsListView.as_view(), name='traditions'),
    path('traditions/<slug:slug>/', TraditionsDetailView.as_view(), name='traditions_detail'),
    path('nominations/', NominationsListView.as_view(), name='nominations'),
    path('nominations/<slug:slug>/', NominationsDetailView.as_view(), name='nominations_detail'),
]
