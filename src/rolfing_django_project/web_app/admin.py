from django.contrib import admin

from .models import TeacherModel, TopicModel, Topic_Module, EventModel, RegionalAssociationModel


@admin.register(TeacherModel)
class TeacherModelAdmin(admin.ModelAdmin):
    ordering = ['second_name', ]


@admin.register(TopicModel)
class TopicModelAdmin(admin.ModelAdmin):
    ordering = ['name', ]


@admin.register(Topic_Module)
class Topic_ModuleAdmin(admin.ModelAdmin):
     ordering = ['topic', 'module', ]


@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    ordering = ['start_date', ]


@admin.register(RegionalAssociationModel)
class RegionalAssociationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'person', ]
    ordering = ['name', ]
    exclude = ['slug', ]
