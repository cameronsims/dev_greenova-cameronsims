# Generated by Django 5.1.6 on 2025-02-20 06:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0009_project_members"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projectmembership",
            options={},
        ),
        migrations.AlterField(
            model_name="projectmembership",
            name="role",
            field=models.CharField(
                choices=[
                    ("owner", "Owner"),
                    ("manager", "Manager"),
                    ("member", "Member"),
                    ("viewer", "Viewer"),
                ],
                default="member",
                help_text="User's role in the project",
                max_length=20,
            ),
        ),
        migrations.AddIndex(
            model_name="projectmembership",
            index=models.Index(
                fields=["user", "project", "role"],
                name="projects_pr_user_id_426451_idx",
            ),
        ),
    ]
