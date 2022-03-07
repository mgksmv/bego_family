from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    paginate_by = 20

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return Employee.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        context['department'] = self.department
        context['object_list'] = object_list

        return context


class DepartmentReglamentsListView(LoginRequiredMixin, ListView):
    model = DepartmentReglament
    template_name = 'departments/department_reglaments.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        department = get_object_or_404(Department, slug=self.kwargs['department'])

        if 'position-instructions' in self.request.path:
            reglament_type = 'Должностные инструкции'
            reglaments = DepartmentReglament.objects.filter(department=department, instruction_type='position_instruction')
        else:
            reglament_type = 'Инструкция по работе'
            reglaments = DepartmentReglament.objects.filter(department=department, instruction_type='job_instruction')

        paginator = Paginator(reglaments, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            reglaments_paginated = paginator.page(page)
        except PageNotAnInteger:
            reglaments_paginated = paginator.page(1)
        except EmptyPage:
            reglaments_paginated = paginator.page(paginator.num_pages)

        context['department'] = department
        context['reglament_type'] = reglament_type
        context['object_list'] = reglaments_paginated

        return context


class DepartmentReglamentsDetailView(LoginRequiredMixin, DetailView):
    model = DepartmentReglament
    template_name = 'detailview_template.html'


class TraineeshipListView(LoginRequiredMixin, ListView):
    model = Traineeship
    template_name = 'departments/traineeship.html'
    paginate_by = 20

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return Traineeship.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            traineeship_paginated = paginator.page(page)
        except PageNotAnInteger:
            traineeship_paginated = paginator.page(1)
        except EmptyPage:
            traineeship_paginated = paginator.page(paginator.num_pages)

        context['object_list'] = traineeship_paginated
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
    paginate_by = 20

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return Training.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            training_paginated = paginator.page(page)
        except PageNotAnInteger:
            training_paginated = paginator.page(1)
        except EmptyPage:
            training_paginated = paginator.page(paginator.num_pages)

        context['object_list'] = training_paginated
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
    paginate_by = 20

    def get_queryset(self):
        self.department = get_object_or_404(Department, slug=self.kwargs['department'])
        return LevelUp.objects.filter(department=self.department)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            levelup_paginated = paginator.page(page)
        except PageNotAnInteger:
            levelup_paginated = paginator.page(1)
        except EmptyPage:
            levelup_paginated = paginator.page(paginator.num_pages)

        context['object_list'] = levelup_paginated
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
