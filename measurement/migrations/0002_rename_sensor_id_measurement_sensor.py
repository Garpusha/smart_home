# Generated by Django 4.2.2 on 2023-06-21 14:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="measurement",
            old_name="sensor_id",
            new_name="sensor",
        ),
    ]
