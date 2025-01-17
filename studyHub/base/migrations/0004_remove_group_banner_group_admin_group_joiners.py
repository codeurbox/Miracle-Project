# Generated by Django 5.0.4 on 2024-05-20 05:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_group_participate_group_banner_group_logo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='banner',
        ),
        migrations.AddField(
            model_name='group',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='joiners',
            field=models.ManyToManyField(blank=True, related_name='joiners', to=settings.AUTH_USER_MODEL),
        ),
    ]
