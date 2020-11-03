from sport_events.notificator.crons.football_api.events import EventsCron
from sport_events.notificator.crons.football_api.teams import TeamsCron
from .notification.email.notifier import EmailNotifier
from .notification.webhook.notifier import WebhookNotifier


def events_1_hour():
    return EventsCron().run()


def teams_1_hour():
    return TeamsCron().run()


def email_7_day():
    return EmailNotifier().cron_7_day()


def email_24_hour():
    return EmailNotifier().cron_24_hour()


def email_live():
    return EmailNotifier().cron_live()


def webhook_7_day():
    return WebhookNotifier().cron_7_day()


def webhook_24_hour():
    return WebhookNotifier().cron_24_hour()


def webhook_live():
    return WebhookNotifier().cron_live()
