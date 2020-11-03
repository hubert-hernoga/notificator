import os
import requests

from datetime import datetime
from notificator.models import Event
from . import api


class EventsCron:
    def __init__(self):
        self.today = datetime.now().strftime("%Y-%m-%d")
        self.url = os.environ["TODAY_EVENT_URL"]
        self.querystring = {"timezone": "Europe/Warsaw"}

    def run(self):
        """
        Adding (updating if exist) teams from first 25 leagues -
        limit for a free plan for Football external API (25 requests / min)
        """
        limit = 0
        try:
            events = list()
            print("===================================")
            print(api.headers)
            response = self.response()

            for event in response["fixtures"]:
                date_obj = datetime.fromisoformat(event["event_date"])
                events.append(Event(
                    league_name=event["league"]["name"],
                    league_country=event["league"]["country"],
                    league_logo=event["league"]["logo"],
                    hour=date_obj.strftime("%H:%M:%S"),
                    date=date_obj.strftime("%Y-%m-%d"),
                    round=event["round"],
                    status=event["status"],
                    venue=event["venue"],
                    home_team_name=event["homeTeam"]["team_name"],
                    home_team_logo=event["homeTeam"]["logo"],
                    goals_home_team=event["goalsHomeTeam"],
                    away_team_name=event["awayTeam"]["team_name"],
                    away_team_logo=event["awayTeam"]["logo"],
                    goals_away_team=event["goalsAwayTeam"],
                ))
            limit += 1

            Event.objects.filter(date=self.today).delete()
            Event.objects.bulk_create(events)
        except Exception as error:
            print(error)
            raise Exception("You made {} requests. Remember that you are limited in the free plan".format(limit))

    def response(self):
        return requests.get(
            self.url.format(date=self.today),
            headers=api.headers,
            params=self.querystring
        ).json()["api"]
