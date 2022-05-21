from modeltranslation.translator import register, TranslationOptions
from .models import Malumot

@register(Malumot)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)