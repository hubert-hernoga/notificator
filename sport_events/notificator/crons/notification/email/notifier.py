from django.core.mail import send_mail
from sport_events.notificator.crons.notification.engine import NotifierEngine


class EmailNotifier:
    def cron_7_day(self):
        notifications = NotifierEngine().notifications("Week", "Email")
        self.sender_generator(notifications)

    def cron_24_hour(self):
        notifications = NotifierEngine().notifications("Day", "Email")
        self.sender_generator(notifications)

    def cron_live(self):
        notifications = NotifierEngine().notifications("Live", "Email")
        self.sender_generator(notifications)

    def sender_generator(self, notifications):
        receivers_per_event = NotifierEngine().receivers_per_event(notifications, "Email")
        for event in receivers_per_event:
            email_list = receivers_per_event[event]
            self.send(event, email_list)

    @staticmethod
    def send(event, email_list):
        message = NotifierEngine().notification_message(event)
        title = 'Stery-notifications'
        sender_name = 'hubert.hernoga@wp.pl'

        send_mail(title, message, sender_name, email_list, fail_silently=False)
