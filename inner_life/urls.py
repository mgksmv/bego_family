from django.urls import path

from .views import GalleryListView, GalleryDetailView, BestEmployeesListView, EmployeeBirthdays

urlpatterns = [
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/<slug:slug>/', GalleryDetailView.as_view(), name='gallery_detail'),
    path('best-employees/', BestEmployeesListView.as_view(), name='best_employees'),
    path('employee-birthdays/', EmployeeBirthdays.as_view(), name='employee_birthdays'),
]
