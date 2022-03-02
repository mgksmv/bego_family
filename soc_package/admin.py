from django.contrib import admin

from .models import SocPackage, Image, Video, PDF


class ImageAdmin(admin.StackedInline):
    model = Image
    extra = 0


class VideoAdmin(admin.StackedInline):
    model = Video
    extra = 0


class PDFAdmin(admin.StackedInline):
    model = PDF
    extra = 0


@admin.register(SocPackage)
class SocPackageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageAdmin, VideoAdmin, PDFAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = SocPackage
