from django.contrib import admin

from .models import Vacancy, Dismissal, Permissions


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('position',)}

    class Meta:
        model = Vacancy


@admin.register(Dismissal)
class DismissalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Dismissal


@admin.register(Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    filter_horizontal = ['permission']
    
    class Meta:
        model = Permissions
