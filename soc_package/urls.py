from django.urls import path

from .views import SocPackageDetailView

urlpatterns = [
    path('<slug:slug>/', SocPackageDetailView.as_view(), name='soc_package_detail'),
]
