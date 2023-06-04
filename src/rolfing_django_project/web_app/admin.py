from django.contrib import admin

from .models import TeacherModel, TopicModel, Topic_Module, EventModel, RegionalAssociationModel, RolfUser


@admin.register(TeacherModel)
class TeacherModelAdmin(admin.ModelAdmin):
    ordering = ['second_name', ]
    exclude = ['second_name', 'first_name', ]  # to exclude default language form


@admin.register(TopicModel)
class TopicModelAdmin(admin.ModelAdmin):
    ordering = ['name', ]
    list_display = ['__str__', ]
    list_display_links = list_display
    list_select_related = True
    exclude = ['name',]

@admin.register(Topic_Module)
class Topic_ModuleAdmin(admin.ModelAdmin):
    ordering = ['-id', 'topic', 'module', ]
    list_display = ['id', '__str__', ]
    list_display_links = list_display
    list_select_related = True
    exclude = ['module', ]


@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    ordering = ['start_date', ]
    list_display = ['id', '__str__', ]
    list_display_links = list_display
    list_select_related = True


@admin.register(RegionalAssociationModel)
class RegionalAssociationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'telephone', 'web_site',]
    list_display_links = ['id', 'name', 'address', 'telephone', ]
    list_select_related = True
    ordering = ['-id', ]
    exclude = ['name', 'address', 'person', ]


@admin.register(RolfUser)
class RolfUserAdmin(admin.ModelAdmin):
    list_display = ['__str__', ]
    list_display_links = list_display
    list_select_related = True
