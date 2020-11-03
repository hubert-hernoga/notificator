import requests
from sport_events.notificator.crons.notification.engine import NotifierEngine


class WebhookNotifier:
    def cron_7_day(self):
        notifications = NotifierEngine().notifications("Week", "Webhook")
        self.sender_generator(notifications)

    def cron_24_hour(self):
        notifications = NotifierEngine().notifications("Day", "Webhook")
        self.sender_generator(notifications)

    def cron_live(self):
        notifications = NotifierEngine().notifications("Live", "Webhook")
        self.sender_generator(notifications)

    def sender_generator(self, notifications):
        receivers_per_event = NotifierEngine().receivers_per_event(notifications, "Webhook")
        for event in receivers_per_event:
            endpoints_list = receivers_per_event[event]
            self.send(event, endpoints_list)

    @staticmethod
    def send(event, endpoints_list):
        message = NotifierEngine().notification_message(event)
        for endpoint in endpoints_list:
            requests.post(endpoint, data=dict(message))
