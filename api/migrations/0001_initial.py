# Generated by Django 4.2.1 on 2023-06-11 03:12

from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IntentionSchedule",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("cron_min", models.CharField(max_length=2)),
                ("cron_hour", models.CharField(max_length=2)),
                ("cron_day_of_month", models.CharField(max_length=2)),
                ("cron_month", models.CharField(max_length=2)),
                ("cron_day_of_week", models.CharField(max_length=2)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Intention",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(verbose_name="Name")),
                (
                    "schedule_tz",
                    timezone_field.fields.TimeZoneField(default="America/New_York"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="intention",
                        to="api.intentionschedule",
                    ),
                ),
                ("user", models.ManyToManyField(to="api.user")),
            ],
        ),
        migrations.CreateModel(
            name="CheckIn",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "intention",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="intention",
                        to="api.intention",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to="api.user",
                    ),
                ),
            ],
        ),
    ]
