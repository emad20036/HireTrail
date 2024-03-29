# Generated by Django 4.2.7 on 2024-01-01 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(blank=True, max_length=50, null=True, unique=True),
                ),
                ("fname", models.CharField(blank=True, max_length=50, null=True)),
                ("lname", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company", models.CharField(max_length=190, null=True)),
                ("position", models.CharField(max_length=190, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("Interview", "Interview"),
                            ("declined", "declined"),
                        ],
                        max_length=190,
                        null=True,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("job_location", models.CharField(max_length=190, null=True)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("full-time", "full-time"),
                            ("part-time", "part-time"),
                            ("internship", "internship"),
                        ],
                        max_length=190,
                        null=True,
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="JobTrack.person",
                    ),
                ),
            ],
        ),
    ]
