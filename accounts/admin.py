from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Position
from .forms import CustomUserCreationForm

CustomUser = get_user_model()


class AccountAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name',
                'last_name',
                'username',
                'email',
                'password1',
                'password2',
                'position',
                'profile_pic',
                'birth_date',
                'is_active',
                'is_staff'),
        }),
    )

    list_display = ('username', 'first_name', 'last_name', 'level', 'email', 'last_login', 'is_active')
    readonly_fields = ('last_login', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.site_header = 'BEGO Family'
admin.site.site_title = 'BEGO Family'

admin.site.unregister(Group)
admin.site.register(CustomUser, AccountAdmin)
admin.site.register(Position)
