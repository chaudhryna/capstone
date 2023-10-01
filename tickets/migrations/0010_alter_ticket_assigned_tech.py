# Generated by Django 4.2.4 on 2023-09-30 12:45

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0009_alter_ticket_assigned_tech'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned_tech',
            field=models.ForeignKey(blank=True, limit_choices_to={django.contrib.auth.models.Group: 'IT Staff'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tech', to=settings.AUTH_USER_MODEL),
        ),
    ]
