from django.contrib import admin

from .models import Gallery, Image, Video


class ImageAdmin(admin.StackedInline):
    model = Image
    extra = 0


class VideoAdmin(admin.StackedInline):
    model = Video
    extra = 0


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageAdmin, VideoAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Gallery
