# Generated by Django 2.2 on 2020-03-20 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stickymessages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stickymessages_message_related_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='message',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stickymessages_message_related_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
    ]
