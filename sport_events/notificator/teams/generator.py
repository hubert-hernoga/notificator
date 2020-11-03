from ..models import Team


class TeamsGenerator:
    teams_obj = Team.objects

    def __init__(self, render, request):
        self.render = render
        self.request = request

    def teams(self):
        return self.render(self.request, "teams/teams.html", {
            "teams": self.teams_obj.all(),
            "quantity": self.teams_obj.count(),
        })
