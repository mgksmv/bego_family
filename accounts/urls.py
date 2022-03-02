from django.urls import path

from .views import ProfileDetailView

urlpatterns = [
    path('<int:profile_id>/', ProfileDetailView.as_view(), name='profile')
]
