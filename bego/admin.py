from django.contrib import admin

from .models import (
    History,
    Mission,
    OrgStructure,
    ImageHistory,
    ImageMission,
    ImageOrgStructure,
    VideoHistory,
    VideoMission,
    VideoOrgStructure,
    PDFHistory,
    PDFMission,
    PDFOrgStructure
)


class ImageHistoryAdmin(admin.StackedInline):
    model = ImageHistory
    extra = 0

class ImageMissionAdmin(admin.StackedInline):
    model = ImageMission
    extra = 0

class ImageOrgStructureAdmin(admin.StackedInline):
    model = ImageOrgStructure
    extra = 0


class VideoHistoryAdmin(admin.StackedInline):
    model = VideoHistory
    extra = 0

class VideoMissionAdmin(admin.StackedInline):
    model = VideoMission
    extra = 0

class VideoOrgStructureAdmin(admin.StackedInline):
    model = VideoOrgStructure
    extra = 0


class PDFHistoryAdmin(admin.StackedInline):
    model = PDFHistory
    extra = 0

class PDFMissionAdmin(admin.StackedInline):
    model = PDFMission
    extra = 0

class PDFOrgStructureAdmin(admin.StackedInline):
    model = PDFOrgStructure
    extra = 0


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageHistoryAdmin, VideoHistoryAdmin, PDFHistoryAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = History


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageMissionAdmin, VideoMissionAdmin, PDFMissionAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Mission


@admin.register(OrgStructure)
class OrgStructureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageOrgStructureAdmin, VideoOrgStructureAdmin, PDFOrgStructureAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = OrgStructure
