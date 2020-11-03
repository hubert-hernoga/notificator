from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .events.generator import EventsGenerator
from .teams.generator import TeamsGenerator
from .notification.generator import NotificationsGenerator
from .registration.generator import Register


def home(request):
    return render(request, "home.html")


def events(request):
    return EventsGenerator(render, request).events()


def future_events(request):
    return EventsGenerator(render, request).future_events()


def ongoing_events(request):
    return EventsGenerator(render, request).ongoing_events()


def past_events(request):
    return EventsGenerator(render, request).past_events()


def teams(request):
    return TeamsGenerator(render, request).teams()


@login_required
def notifications(request):
    return NotificationsGenerator(render, request, redirect).save()


def notifications_success_page(request):
    return NotificationsGenerator(render, request, redirect).success()


def register(request):
    return Register(render, request, redirect).run()
