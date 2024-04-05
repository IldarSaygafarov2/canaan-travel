from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(models.Destination)
class DestinationTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description')


@register(models.Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt')