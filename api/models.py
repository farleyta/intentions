import uuid
from django.db import models
from timezone_field import TimeZoneField


class Intention_Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cron_min = models.CharField(max_length=5, default="*")
    # All crons are stored in UTC!
    cron_hour = models.CharField(max_length=5, default="*")
    cron_day_of_month = models.CharField(max_length=5, default="*")
    cron_month = models.CharField(max_length=5, default="*")
    cron_day_of_week = models.CharField(max_length=5, default="*")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Intention(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name")
    schedule = models.ForeignKey(
        Intention_Schedule, related_name="intention", on_delete=models.PROTECT
    )
    schedule_tz = TimeZoneField(default="America/New_York")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    intentions = models.ManyToManyField(Intention, related_name="user")

    def __str__(self):
        return self.id


class CheckIn(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    intention = models.ForeignKey(
        Intention, related_name="intention", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
