from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


# Register your models here.

class ReviewAdmin(TranslationAdmin):
    list_display = ('author', 'text')


class TourAdmin(TranslationAdmin):
    list_display = ('title', 'price', 'days', 'nights', 'preview', 'is_popular', 'is_recommended', 'destination')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('destination',)
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
admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.Advantage, AdvantageAdmin)
admin.site.register(models.Destination, DestinationAdmin)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.Article, ArticleAdmin)
