from sport_events.notificator.models import Notification


class NotifierEngine:
    def receivers_per_event(self, notifications, receiver_type):
        result = dict()
        for notification in notifications:
            event = notification.event
            receiver = self.receiver(notification, receiver_type)

            if event in result and receiver not in result[event]:
                result[event].append(receiver)
            else:
                result[event] = [receiver]

        return result

    @staticmethod
    def receiver(notification, receiver_type):
        receiver = notification.endpoint
        if receiver_type == "Email":
            receiver = notification.user.email

        return receiver

    @staticmethod
    def notifications(frequency, type):
        return Notification.objects.filter(frequency=frequency, type=type)

    @staticmethod
    def notification_message(event):
        match = str(event.round)
        date = str(event.date)
        hour = str(event.hour)
        return "Match - " + match + " will be " + date + " at " + hour
