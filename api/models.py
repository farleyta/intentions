from django.db import models
from timezone_field import TimeZoneField


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    email = models.EmailField(unique=True, max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Intention(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField("Name")
    user = models.ManyToManyField(User)
    schedule_tz = TimeZoneField(default="America/New_York")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class IntentionSchedule(models.Model):
    id = models.UUIDField(primary_key=True)
    intention = models.ForeignKey(Intention, related_name="schedule")
    cron_min = models.CharField(max_length=2)
    cron_hour = models.CharField(max_length=2)
    cron_day_of_month = models.CharField(max_length=2)
    cron_month = models.CharField(max_length=2)
    cron_day_of_week = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class CheckIn(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, related_name="user")
    intention = models.ForeignKey(Intention, related_name="intention")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
