from django.urls import reverse
from django.contrib.auth import login
from ..models import Event
from ..forms import UserCreateForm


class Register:
    events_obj = Event.objects

    def __init__(self, render, request, redirect):
        self.render = render
        self.request = request
        self.redirect = redirect

    def get(self):
        return self.render(
            self.request,
            "registration/register.html", {
                "form": UserCreateForm
            }
        )

    def post(self):
        form = UserCreateForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            return self.redirect(reverse("home"))
        return self.render(self.request, "registration/register.html", {"form": form})

    def run(self):
        if self.request.method == "GET":
            return self.get()

        elif self.request.method == "POST":
            return self.post()
