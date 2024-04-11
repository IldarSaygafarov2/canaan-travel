from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


# Register your models here.


class TourAdmin(TranslationAdmin):
    list_display = ('title', 'price', 'days', 'nights', 'is_popular', 'is_recommended')
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(TranslationAdmin):
    pass


class DestinationAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AdvantageAdmin(TranslationAdmin):
    pass


admin.site.register(models.Review)
admin.site.register(models.Client)
admin.site.register(models.Advantage, AdvantageAdmin)
admin.site.register(models.Destination, DestinationAdmin)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.Article, ArticleAdmin)
