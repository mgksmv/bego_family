from django.urls import path

from .views import HistoryDetailView, MissionDetailView, OrgStructureDetailView

urlpatterns = [
    path('history/<slug:slug>/', HistoryDetailView.as_view(), name='history'),
    path('mission/<slug:slug>/', MissionDetailView.as_view(), name='mission'),
    path('org-structure/<slug:slug>/', OrgStructureDetailView.as_view(), name='org_structure'),
]
