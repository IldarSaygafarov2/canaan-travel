from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('author', 'text')


@register(models.HotelItem)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(models.Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'full_description')


@register(models.Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(models.Destination)
class DestinationTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description')


@register(models.Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt')
