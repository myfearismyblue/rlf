# Generated by Django 4.1 on 2023-06-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='events', to='web_app.teachermodel'),
        ),
    ]