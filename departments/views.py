from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import (
    Presentation,
    Department,
    Employee,
    DepartmentReglament,
    Traineeship,
    VideoTraineeship,

    Training,
    ImageTraining,
    VideoTraining,
    PDFTraining,

    LevelUp,
    ImageLevelUp,
    VideoLevelUp,
    PDFLevelUp
)


class PresentationDetailView(LoginRequiredMixin, DetailView):
    model = Presentation
    template_name = 'departments/presentation.html'

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return Presentation.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.department
        return context


class EmployeesListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'departments/employees.html'

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return Employee.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.department
        return context


class DepartmentReglamentsListView(LoginRequiredMixin, ListView):
    model = DepartmentReglament
    template_name = 'departments/department_reglaments.html'

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        if 'position-instructions' in self.request.path:
            self.reglament_type = 'Должностные инструкции'
            self.reglaments = DepartmentReglament.objects.filter(department=self.department, instruction_type='position_instruction')
        else:
            self.reglament_type = 'Инструкция по работе'
            self.reglaments = DepartmentReglament.objects.filter(department=self.department, instruction_type='job_instruction')
        return self.reglaments

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.department
        context['reglament_type'] = self.reglament_type
        return context


class DepartmentReglamentsDetailView(LoginRequiredMixin, DetailView):
    model = DepartmentReglament
    template_name = 'detailview_template.html'


class TraineeshipListView(LoginRequiredMixin, ListView):
    model = Traineeship
    template_name = 'departments/traineeship.html'

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return Traineeship.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.department
        return context


class TraineeshipDetailView(LoginRequiredMixin, DetailView):
    model = Traineeship
    template_name = 'departments/traineeship_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = VideoTraineeship.objects.filter(parent_model=self.object)
        return context


class TrainingListView(LoginRequiredMixin, ListView):
    model = Training
    template_name = 'departments/training.html'

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return Training.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.department
        return context


class TrainingDetailView(LoginRequiredMixin, DetailView):
    model = Training
    template_name = 'departments/training_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ImageTraining.objects.filter(parent_model=self.object)
        context['videos'] = VideoTraining.objects.filter(parent_model=self.object)
        context['pdfs'] = PDFTraining.objects.filter(parent_model=self.object)
        return context


class LevelUpListView(LoginRequiredMixin, ListView):
    model = LevelUp
    template_name = 'departments/levelup.html'

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return LevelUp.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.department
        return context


class LevelUpDetailView(LoginRequiredMixin, DetailView):
    model = LevelUp
    template_name = 'departments/levelup_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ImageLevelUp.objects.filter(parent_model=self.object)
        context['videos'] = VideoLevelUp.objects.filter(parent_model=self.object)
        context['pdfs'] = PDFLevelUp.objects.filter(parent_model=self.object)
        return context


class PositioningDetailView(LoginRequiredMixin, DetailView):
    model = Department
    template_name = 'departments/positioning.html'
