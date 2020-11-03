from .save import Notificator
from ..forms import NotificationsForm
from ..models import Event


class NotificationsGenerator:
    events_obj = Event.objects

    def __init__(self, render, request, redirect):
        self.render = render
        self.request = request
        self.redirect = redirect

    def save(self):
        # if this is a POST request we need to process the form data
        if self.request.method == 'POST':

            # create a form instance and populate it with data from the request:
            form = NotificationsForm(self.request.POST)

            # check whether it's valid:
            if form.is_valid():

                # process the data in form.cleaned_data as required
                Notificator(form, self.request).save(self.events_obj)

                return self.redirect("/notification/success")
            return self.render(self.request, "notification/notification.html", {"form": form})
        return self.render(self.request, "notification/notification.html", {"form": NotificationsForm})

    def success(self):
        return self.render(self.request, "notification/success_page.html")
