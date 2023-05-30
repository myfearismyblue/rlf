from django.contrib import admin

from .models import TeacherModel, TopicModel, Topic_Module, EventModel, RegionalAssociationModel


@admin.register(TeacherModel)
class TeacherModelAdmin(admin.ModelAdmin):
    ordering = ['second_name', ]
    exclude = ['second_name', 'first_name', ]  # to exclude default language form


@admin.register(TopicModel)
class TopicModelAdmin(admin.ModelAdmin):
    ordering = ['name', ]
    list_display = ['id', '__str__', ]
    exclude = ['name',]

@admin.register(Topic_Module)
class Topic_ModuleAdmin(admin.ModelAdmin):
    ordering = ['topic', 'module', ]
    list_display = ['id', '__str__', ]
    exclude = ['module', ]


@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    ordering = ['start_date', ]
    list_display = ['id', '__str__', ]


@admin.register(RegionalAssociationModel)
class RegionalAssociationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'person', ]
    ordering = ['name', ]
    exclude = ['slug', 'name', 'address', 'person']
