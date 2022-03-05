from django.contrib import admin

from .models import (
    Department,
    Presentation,
    Employee,
    DepartmentReglament,
    Traineeship,
    ImageDepartmentReglament,
    VideoDepartmentReglament,
    PDFDepartmentReglament,
    ImageTraineeship,
    VideoTraineeship,
    PDFTraineeship,
    Training,
    LevelUp,
    ImageTraining,
    VideoTraining,
    PDFTraining,
    ImageLevelUp,
    VideoLevelUp,
    PDFLevelUp
)


class PresentationAdmin(admin.TabularInline):
    model = Presentation
    extra = 0


class EmployeeStackedInLine(admin.TabularInline):
    model = Employee
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    extra = 0


class DepartmentReglamentStackedInLine(admin.TabularInline):
    model = DepartmentReglament
    prepopulated_fields = {'slug': ('name',)}
    extra = 0


class ImageDepartmentReglamentAdmin(admin.StackedInline):
    model = ImageDepartmentReglament
    extra = 0

class VideoDepartmentReglamentAdmin(admin.StackedInline):
    model = VideoDepartmentReglament
    extra = 0

class PDFDepartmentReglamentAdmin(admin.StackedInline):
    model = PDFDepartmentReglament
    extra = 0


class ImageTraineeshipAdmin(admin.StackedInline):
    model = ImageTraineeship
    extra = 0

class VideoTraineeshipAdmin(admin.StackedInline):
    model = VideoTraineeship
    extra = 0

class PDFTraineeshipAdmin(admin.StackedInline):
    model = PDFTraineeship
    extra = 0


class ImageTrainingAdmin(admin.StackedInline):
    model = ImageTraining
    extra = 0

class VideoTrainingAdmin(admin.StackedInline):
    model = VideoTraining
    extra = 0

class PDFTrainingAdmin(admin.StackedInline):
    model = PDFTraining
    extra = 0


class ImageLevelUpAdmin(admin.StackedInline):
    model = ImageLevelUp
    extra = 0

class VideoLevelUpAdmin(admin.StackedInline):
    model = VideoLevelUp
    extra = 0

class PDFLevelUpAdmin(admin.StackedInline):
    model = PDFLevelUp
    extra = 0


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['access']
    inlines = [PresentationAdmin, EmployeeStackedInLine, DepartmentReglamentStackedInLine]

    class Meta:
        model = Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ['full_name', 'department', 'position']
    list_filter = ['department', 'position']
    list_editable = ['department', 'position']
    search_fields = ['first_name', 'last_name', 'middle_name']

    def full_name(self, obj):
        return obj.get_full_name()
    full_name.short_description = 'ФИО'

    class Meta:
        model = Employee


@admin.register(DepartmentReglament)
class DepartmentReglamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageDepartmentReglamentAdmin, VideoDepartmentReglamentAdmin, PDFDepartmentReglamentAdmin]
    filter_horizontal = ['access']
    list_display = ['name', 'department', 'instruction_type']
    list_editable = ['department', 'instruction_type']
    list_filter = ['department', 'instruction_type']

    class Meta:
        model = DepartmentReglament


@admin.register(Traineeship)
class TraineeshipAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageTraineeshipAdmin, VideoTraineeshipAdmin, PDFTraineeshipAdmin]
    filter_horizontal = ['access']
    list_display = ['name', 'department', 'day', 'prev_url', 'next_url']
    list_editable = ['department', 'day', 'prev_url', 'next_url']
    list_filter = ['department', 'access']

    class Meta:
        model = Traineeship


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['access']
    inlines = [ImageTrainingAdmin, VideoTrainingAdmin, PDFTrainingAdmin]

    class Meta:
        model = Training


@admin.register(LevelUp)
class LevelUpAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['access']
    inlines = [ImageLevelUpAdmin, VideoLevelUpAdmin, PDFLevelUpAdmin]

    class Meta:
        model = LevelUp


admin.site.register(Presentation)
