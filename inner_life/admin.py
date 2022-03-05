from django.contrib import admin

from .models import (
    Gallery,
    GalleryImage,
    GalleryVideo,
    BestEmployee,
    Event,
    RecordBook,
    Video,
    Giveaway,
    Tradition,
    Nomination,
    ImageRecordBook,
    VideoRecordBook,
    PDFRecordBook,
    ImageVideo,
    VideoVideo,
    PDFVideo,
    ImageGiveaway,
    VideoGiveaway,
    PDFGiveaway,
    ImageTradition,
    VideoTradition,
    PDFTradition,
    ImageNomination,
    VideoNomination,
    PDFNomination
)


class ImageAdmin(admin.StackedInline):
    model = GalleryImage
    extra = 0


class VideoAdmin(admin.StackedInline):
    model = GalleryVideo
    extra = 0


class ImageRecordBookAdmin(admin.StackedInline):
    model = ImageRecordBook
    extra = 0

class ImageVideoAdmin(admin.StackedInline):
    model = ImageVideo
    extra = 0

class ImageGiveawayAdmin(admin.StackedInline):
    model = ImageGiveaway
    extra = 0

class ImageTraditionAdmin(admin.StackedInline):
    model = ImageTradition
    extra = 0

class ImageNominationAdmin(admin.StackedInline):
    model = ImageNomination
    extra = 0


class VideoRecordBookAdmin(admin.StackedInline):
    model = VideoRecordBook
    extra = 0

class VideoVideoAdmin(admin.StackedInline):
    model = VideoVideo
    extra = 0

class VideoGiveawayAdmin(admin.StackedInline):
    model = VideoGiveaway
    extra = 0

class VideoTraditionAdmin(admin.StackedInline):
    model = VideoTradition
    extra = 0

class VideoNominationAdmin(admin.StackedInline):
    model = VideoNomination
    extra = 0


class PDFRecordBookAdmin(admin.StackedInline):
    model = PDFRecordBook
    extra = 0

class PDFVideoAdmin(admin.StackedInline):
    model = PDFVideo
    extra = 0

class PDFGiveawayAdmin(admin.StackedInline):
    model = PDFGiveaway
    extra = 0

class PDFTraditionAdmin(admin.StackedInline):
    model = PDFTradition
    extra = 0

class PDFNominationAdmin(admin.StackedInline):
    model = PDFNomination
    extra = 0


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageAdmin, VideoAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Gallery


@admin.register(BestEmployee)
class BestEmployeeAdmin(admin.ModelAdmin):
    filter_horizontal = ['access']

    class Meta:
        model = BestEmployee

    
@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['access', 'participants']
    list_display = ['name', 'date', 'department']
    list_editable = ['date', 'department']
    list_filter = ['department', 'access']

    class Meta:
        model = Event


@admin.register(RecordBook)
class RecordBookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageRecordBookAdmin, VideoRecordBookAdmin, PDFRecordBookAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = RecordBook


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageVideoAdmin, VideoVideoAdmin, PDFVideoAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Video


@admin.register(Giveaway)
class GiveawayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageGiveawayAdmin, VideoGiveawayAdmin, PDFGiveawayAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Giveaway


@admin.register(Tradition)
class TraditionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageTraditionAdmin, VideoTraditionAdmin, PDFTraditionAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Tradition


@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageNominationAdmin, VideoNominationAdmin, PDFNominationAdmin]
    filter_horizontal = ['access']

    class Meta:
        model = Nomination
