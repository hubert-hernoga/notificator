"""django_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from .views import *

event_urlpatterns = [
    path('all/', events, name="events"),
    path('future-events/', future_events, name="future_events"),
    path('ongoing-events/', ongoing_events, name="ongoing_events"),
    path('past-events/', past_events, name="past_events"),
]

team_urlpatterns = [
    path('all', teams, name="teams"),
]

notification_urlpatterns = [
    path('sign-up', notifications, name="notification"),
    path('success', notifications_success_page, name="success_page"),
]

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^events/", include(event_urlpatterns)),
    url(r"^teams/", include(team_urlpatterns)),
    url(r"^notification/", include(notification_urlpatterns)),
    url(r"^register/", register, name="register"),
]
