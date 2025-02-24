# Generated by Django 5.1.6 on 2025-02-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mechanisms", "0004_alter_environmentalmechanism_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="environmentalmechanism",
            name="created_at",
        ),
        migrations.AlterField(
            model_name="environmentalmechanism",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="environmentalmechanism",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="environmentalmechanism",
            name="status",
            field=models.CharField(
                choices=[
                    ("not started", "Not Started"),
                    ("in progress", "In Progress"),
                    ("completed", "Completed"),
                ],
                max_length=20,
            ),
        ),
    ]
