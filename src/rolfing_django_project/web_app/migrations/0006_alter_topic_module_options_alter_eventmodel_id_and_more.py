# Generated by Django 4.1 on 2023-06-04 21:05

from django.db import migrations, models
import functools
import web_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic_module',
            options={'verbose_name': 'Module', 'verbose_name_plural': 'Modules'},
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='id',
            field=models.IntegerField(default=functools.partial(web_app.models._id_autofill, *(), **{'qualname': 'EventModel'}), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='regionalassociationmodel',
            name='id',
            field=models.IntegerField(default=functools.partial(web_app.models._id_autofill, *(), **{'qualname': 'RegionalAssociationModel'}), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='id',
            field=models.IntegerField(default=functools.partial(web_app.models._id_autofill, *(), **{'qualname': 'TeacherModel'}), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic_module',
            name='id',
            field=models.IntegerField(default=functools.partial(web_app.models._id_autofill, *(), **{'qualname': 'Topic_Module'}), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topicmodel',
            name='id',
            field=models.IntegerField(default=functools.partial(web_app.models._id_autofill, *(), **{'qualname': 'TopicModel'}), primary_key=True, serialize=False),
        ),
    ]