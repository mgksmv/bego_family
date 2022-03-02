from django.contrib import admin

from .models import (
    Reglament,
    Penalty,
    Bonus,
    ImageReglament,
    ImageBonus,
    ImagePenalty,
    VideoReglament,
    VideoBonus,
    VideoPenalty,
    PDFReglament,
    PDFBonus,
    PDFPenalty
)


class ImageReglamentAdmin(admin.StackedInline):
    model = ImageReglament
    extra = 0

class ImageBonusAdmin(admin.StackedInline):
    model = ImageBonus
    extra = 0

class ImagePenaltyAdmin(admin.StackedInline):
    model = ImagePenalty
    extra = 0


class VideoReglamentAdmin(admin.StackedInline):
    model = VideoReglament
    extra = 0

class VideoBonusAdmin(admin.StackedInline):
    model = VideoBonus
    extra = 0

class VideoPenaltyAdmin(admin.StackedInline):
    model = VideoPenalty
    extra = 0


class PDFReglamentAdmin(admin.StackedInline):
    model = PDFReglament
    extra = 0

class PDFBonusAdmin(admin.StackedInline):
    model = PDFBonus
    extra = 0

class PDFPenaltyAdmin(admin.StackedInline):
    model = PDFPenalty
    extra = 0


@admin.register(Reglament)
class ReglamentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageReglamentAdmin, VideoReglamentAdmin, PDFReglamentAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Reglament


@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImagePenaltyAdmin, VideoPenaltyAdmin, PDFPenaltyAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Penalty


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageBonusAdmin, VideoBonusAdmin, PDFBonusAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Bonus
