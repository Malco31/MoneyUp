# Generated by Django 4.1.2 on 2022-11-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_entry_hours_alter_entry_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
