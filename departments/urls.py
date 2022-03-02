from django.urls import path

from .views import (
    PresentationDetailView,
    EmployeesListView,
    DepartmentReglamentsListView,
    DepartmentReglamentsDetailView,
    TraineeshipListView,
    TraineeshipDetailView,
    TrainingListView,
    TrainingDetailView,
    LevelUpListView,
    LevelUpDetailView
)

urlpatterns = [
    path('<department>/presentation/<pk>', PresentationDetailView.as_view(), name='presentation'),
    path('<department>/employees/', EmployeesListView.as_view(), name='employees'),
    path('<department>/position-instructions/', DepartmentReglamentsListView.as_view(), name='position_instructions'),
    path('<department>/position-instructions/<slug>/', DepartmentReglamentsDetailView.as_view(), name='position_instructions_detail'),
    path('<department>/job-instructions/', DepartmentReglamentsListView.as_view(), name='job_instructions'),
    path('<department>/job-instructions/<slug>/', DepartmentReglamentsDetailView.as_view(), name='job_instructions_detail'),
    path('<department>/traineeship/', TraineeshipListView.as_view(), name='traineeship'),
    path('<department>/traineeship/<slug>/', TraineeshipDetailView.as_view(), name='traineeship_detail'),
    path('<department>/training/', TrainingListView.as_view(), name='training'),
    path('<department>/training/<slug>/', TrainingDetailView.as_view(), name='training_detail'),
    path('<department>/level-up/', LevelUpListView.as_view(), name='levelup'),
    path('<department>/level-up/<slug>/', LevelUpDetailView.as_view(), name='levelup_detail'),
]
