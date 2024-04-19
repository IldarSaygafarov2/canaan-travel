from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


# Register your models here.

class ReviewAdmin(TranslationAdmin):
    list_display = ('author', 'text')


# TourWithPrice inlines start
class PlacesTourWithPriceInline(admin.TabularInline):
    model = models.PlacesTourWithPrice
    extra = 1


class DayTourWithPriceInline(admin.TabularInline):
    model = models.DayTourWithPrice
    extra = 1


class AddonTourWithPriceInline(admin.TabularInline):
    model = models.AddonTourWithPrice
    extra = 1


class TourConditionInline(admin.TabularInline):
    model = models.TourCondition
    extra = 1


class TourHotelInline(admin.TabularInline):
    model = models.TourHotel
    extra = 1


class TourPriceIncludeInline(admin.TabularInline):
    model = models.TourPriceInclude
    extra = 1


class TourPriceDoesNotIncludeInline(admin.TabularInline):
    model = models.TourPriceDoesNotInclude
    extra = 1


class PriceByHumanTourInline(admin.TabularInline):
    model = models.PriceByHumanTour
    extra = 1
# TourWithPrice inlines end


class TourAdmin(TranslationAdmin):
    list_display = ('title', 'preview', 'is_popular', 'is_recommended', 'destination')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('destination',)
    list_editable = ('is_popular', 'is_recommended')


class TourWithPriceAdmin(TranslationAdmin):
    list_display = ('title', 'price', 'days', 'nights', 'is_popular', 'is_recommended')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        PlacesTourWithPriceInline,
        DayTourWithPriceInline,
        AddonTourWithPriceInline,
        TourConditionInline,
        TourHotelInline,
        TourPriceIncludeInline,
        TourPriceDoesNotIncludeInline,
        PriceByHumanTourInline,

    ]
    list_editable = ('is_popular', 'is_recommended')


class ArticleAdmin(TranslationAdmin):
    pass


class DestinationAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AdvantageAdmin(TranslationAdmin):
    pass


class HotelAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.Client)
admin.site.register(models.HotelItem, HotelAdmin)
admin.site.register(models.Advantage, AdvantageAdmin)
admin.site.register(models.Destination, DestinationAdmin)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.TourWithPrice, TourWithPriceAdmin)
admin.site.register(models.Article, ArticleAdmin)
