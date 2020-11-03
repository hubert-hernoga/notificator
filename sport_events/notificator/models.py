from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail


class Event(models.Model):
    league_name = models.CharField(max_length=255)
    league_country = models.CharField(max_length=255)
    league_logo = models.URLField(max_length=255, blank=True)
    date = models.DateField(blank=True, db_index=True)
    hour = models.TimeField(auto_now_add=False)
    round = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    venue = models.CharField(max_length=255, null=True)
    home_team_name = models.CharField(max_length=255)
    home_team_logo = models.URLField(max_length=255, blank=True)
    goals_home_team = models.IntegerField(null=True)
    away_team_name = models.CharField(max_length=255, null=True)
    away_team_logo = models.URLField(max_length=255, blank=True)
    goals_away_team = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{home_team_name} vs {away_team_name} | {date} | {hour}'.format(
            home_team_name=self.home_team_name,
            away_team_name=self.away_team_name,
            date=self.date,
            hour=self.hour
        )


class Team(models.Model):
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=10, null=True)
    logo = models.URLField(max_length=255, blank=True)
    country = models.CharField(max_length=255, null=True)
    is_national = models.BooleanField(default=False)
    founded = models.IntegerField(null=True)
    venue_name = models.CharField(max_length=255, null=True)
    venue_surface = models.CharField(max_length=255, null=True)
    venue_address = models.CharField(max_length=255, null=True)
    venue_city = models.CharField(max_length=255, null=True)
    venue_capacity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    TYPES = (
        ('Webhook', 'Webhook'),
        ('Email', 'Email')
    )
    FREQ = (
        ('Week', 'Weekly'),
        ('Day', 'Daily'),
        ('Live', 'Live')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='notifications')
    enabled = models.BooleanField(default=True)
    endpoint = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=10, choices=TYPES, db_index=True,)
    frequency = models.CharField(max_length=10, choices=FREQ)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        user = User.objects.get(id=self.user.id)
        event = Event.objects.get(id=self.event.id)
        message = 'Hello {user}! Congratulations! \n' \
                  'You just signed up for the notification at the match \n' \
                  '{home_team} vs {away_team} at {hour} {date}' \
                  .format(user=user.username,
                          home_team=event.home_team_name,
                          away_team=event.away_team_name,
                          hour=event.hour,
                          date=event.date,
                          )

        send_mail(
            'Sport event notifications',
            message,
            'hubert.hernoga@wp.pl',
            ['hubert.hernoga@gmail.com'],
            fail_silently=False
        )
