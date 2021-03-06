# Generated by Django 2.2.9 on 2020-01-20 22:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailforms', '0003_capitalizeverbose'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='BlogIndexPage',
        ),
        migrations.RenameField(
            model_name='blogindexpage',
            old_name='body',
            new_name='intro',
        ),
    ]
