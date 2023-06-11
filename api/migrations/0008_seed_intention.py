# Generated by Django 4.2.1 on 2023-06-11 23:11

from django.db import migrations


def seed_data(apps, schema_editor):
    User = apps.get_model("api", "User")
    User(email="farleyta@gmail.com").save()
    u = User.objects.filter(email="farleyta@gmail.com").first()

    Intention_Schedule = apps.get_model("api", "Intention_Schedule")
    Intention_Schedule(cron_min=0, cron_hour=12).save()
    s = Intention_Schedule.objects.filter(cron_hour="12").first()

    Intention = apps.get_model("api", "Intention")
    i = Intention(name="TEST: Daily Report", schedule=s)
    i.save()

    u.intentions.add(i)
    u.save()


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_rename_intentionschedule_intention_schedule_and_more"),
    ]

    operations = [migrations.RunPython(seed_data)]
