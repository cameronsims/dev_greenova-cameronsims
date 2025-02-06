# Generated by Django 5.1.5 on 2025-01-26 06:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Obligation",
            fields=[
                (
                    "obligation_number",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "project_name",
                    models.CharField(
                        choices=[
                            ("Portside", "Portside"),
                            ("WA6946", "WA6946"),
                            ("MS1180", "MS1180"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "primary_environmental_mechanism",
                    models.TextField(blank=True, null=True),
                ),
                ("procedure", models.TextField(blank=True, null=True)),
                ("environmental_aspect", models.TextField(blank=True, null=True)),
                ("obligation", models.TextField()),
                ("accountability", models.CharField(max_length=255)),
                ("project_phase", models.TextField()),
                ("action_due_date", models.DateField(blank=True, null=True)),
                ("close_out_date", models.DateField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("not started", "Not Started"),
                            ("in progress", "In Progress"),
                            ("completed", "Completed"),
                            ("overdue", "Overdue"),
                        ],
                        default="not started",
                        max_length=50,
                    ),
                ),
                ("supporting_information", models.TextField(blank=True, null=True)),
                ("general_comments", models.TextField(blank=True, null=True)),
                ("compliance_comments", models.TextField(blank=True, null=True)),
                ("non_conformance_comments", models.TextField(blank=True, null=True)),
                ("evidence", models.TextField(blank=True, null=True)),
                (
                    "person_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("recurring_obligation", models.BooleanField(default=False)),
                (
                    "recurring_frequency",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "recurring_status",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("recurring_forcasted_date", models.DateField(blank=True, null=True)),
                ("inspection", models.BooleanField(default=False)),
                (
                    "inspection_frequency",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "site_or_desktop",
                    models.CharField(
                        blank=True,
                        choices=[("Site", "Site"), ("Desktop", "Desktop")],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("new_control_action_required", models.BooleanField(default=False)),
                (
                    "obligation_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("gap_analysis", models.TextField(blank=True, null=True)),
                ("notes_for_gap_analysis", models.TextField(blank=True, null=True)),
                (
                    "covered_in_which_inspection_checklist",
                    models.TextField(blank=True, null=True),
                ),
                (
                    "responsibility",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assigned_obligations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["action_due_date", "obligation_number"],
            },
        ),
    ]
