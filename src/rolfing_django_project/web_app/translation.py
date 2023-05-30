# responsible for db content translations


from modeltranslation.translator import register, TranslationOptions
from .models import TeacherModel, TopicModel, Topic_Module, RegionalAssociationModel


@register(TeacherModel)
class TeacherModelTranslationOptions(TranslationOptions):
    fields = ('first_name', 'second_name',)


@register(TopicModel)
class TopicModelTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Topic_Module)
class Topic_ModuleTranslationOptions(TranslationOptions):
    fields = ('module',)


@register(RegionalAssociationModel)
class RegionalAssociationModelTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'person', )
