# Generated by Django 4.2.4 on 2023-09-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]