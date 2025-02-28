# Generated by Django 5.1.6 on 2025-02-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projectmembership_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmembership',
            name='role',
            field=models.CharField(choices=[('owner', 'Owner'), ('manager', 'Manager'), ('member', 'Member'), ('viewer', 'Viewer'), ('simon', 'Simon')], default='member', max_length=20),
        ),
    ]
