# Generated by Django 4.1 on 2023-05-15 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_alter_regionalassociationmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionalassociationmodel',
            name='telephone',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='regionalassociationmodel',
            name='web_site',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]