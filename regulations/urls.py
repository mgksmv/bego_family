from django.urls import path

from .views import ReglamentDetailView, PenaltyDetailView, BonusDetailView

urlpatterns = [
    path('reglaments/<slug:slug>/', ReglamentDetailView.as_view(), name='reglament'),
    path('penalties/<slug:slug>/', PenaltyDetailView.as_view(), name='penalty'),
    path('bonuses/<slug:slug>/', BonusDetailView.as_view(), name='bonus'),
]
