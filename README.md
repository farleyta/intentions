# intentions
A hobby project for setting and checking in on personal intentions

# data model
first-draft, has since been revised a bit
https://drawsql.app/teams/personal-916/diagrams/intentions

# TODO:
 - create a IntentionType model for Count, Boolean
 - adjust check-in schema to allow free-form JSON (count, true/false)
 - create concept of Daily vs The Next Day (on IntentionSchedule?)
 - [rest api](https://blog.logrocket.com/using-react-django-create-app-tutorial/)
 - create cron to check intention schedules and make check-ins
 - when making a check-in, need a new field to differentiate same-day from yesterday checkins
 - add a "complete" flag to check-ins, or use presence/absence of json data to derive whether it has been submitted?
 - add a UI for filling in created check-ins? or a way to send/receive checkins via email/sms/app?
 - auth
 - host this somewhere?

# .env
https://django-environ.readthedocs.io/en/latest/quickstart.html

# django-extensions
https://django-extensions.readthedocs.io/en/latest/index.html