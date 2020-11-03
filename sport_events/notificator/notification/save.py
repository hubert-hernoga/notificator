from ..models import Notification, User


class Notificator:
    def __init__(self, form, request):
        self.form = form
        self.request = request

    def save(self, events):
        user = User.objects.get(id=self.request.user.id)
        event = events.get(id=self.form.cleaned_data['event'].id)
        frequency = self.form.cleaned_data['frequency']
        endpoint = self.form.cleaned_data['endpoint']
        type = self.form.cleaned_data['type']
        enabled = self.form.cleaned_data['enabled']

        n = Notification(user=user,
                         event=event,
                         frequency=frequency,
                         type=type,
                         enabled=enabled,
                         endpoint=endpoint
                         )
        n.save()
