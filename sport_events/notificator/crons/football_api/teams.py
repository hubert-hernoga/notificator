import os
import requests

from sport_events.notificator.crons.football_api.api import headers
from sport_events.notificator.models import Team


class TeamsCron:
    def __init__(self):
        self.url = os.environ["LEAGUE_URL"]

    def run(self):
        """
        Adding (updating if exist) teams from first 30 leagues -
        limit for a free plan for Football external API (25 requests / min)
        """
        league_id = 1
        try:
            teams = list()
            while league_id != 25:

                response = self.response(league_id)
                for team in response["teams"]:
                    teams.append(Team(
                        name=team["name"],
                        code=team["code"],
                        logo=team["logo"],
                        country=team["country"],
                        is_national=team["is_national"],
                        founded=team["founded"],
                        venue_name=team["venue_name"],
                        venue_surface=team["venue_surface"],
                        venue_address=team["venue_address"],
                        venue_city=team["venue_city"],
                        venue_capacity=team["venue_capacity"]
                    ))
                league_id += 1

            Team.objects.bulk_create(teams)
        except Exception as error:
            print(error)
            raise Exception("You made {} requests. Remember that you are limited in the free plan".format(league_id))

    def response(self, league_id):
        return requests.get(
            self.url.format(league_id=league_id),
            headers=headers
        ).json()["api"]
