from datetime import datetime
from ..models import Event
from ..crons.football_api.events import EventsCron


class EventsGenerator:
    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    events_obj = Event.objects

    def __init__(self, render, request):
        self.render = render
        self.request = request

    def events(self, ):
        return self.render(self.request, "events/events.html", {
            "quantity": self.events_obj.count(),
        })

    def future_events(self):
        f_events = list(filter(lambda event: "Half" not in event.status and
                                             str(event.date) > self.today or
                                             str(event.date) == self.today and
                                             str(event.hour) > self.current_time,
                               self.events_obj.all().order_by('date')))

        return self.render(self.request, "events/future_events.html", {
            "future_events": f_events,
            "quantity": len(f_events)
        })

    def ongoing_events(self):
        t_events = list(filter(lambda event: "Half" in event.status and
                                             str(event.date) == self.today,
                               self.events_obj.all().order_by('date')))

        # Ugly hack. Don't judge me - getting only today's events
        EventsCron().run()
        return self.render(self.request, "events/ongoing_events.html", {
            "ongoing_events": t_events,
            "quantity": len(t_events)
        })

    def past_events(self):
        p_events = list(filter(lambda event: "Half" not in event.status and
                                             "Started" not in event.status and
                                             str(event.date) < self.today or
                                             str(event.date) == self.today and
                                             str(event.hour) < self.current_time,
                               self.events_obj.all().order_by('-date')))
        return self.render(self.request, "events/past_events.html", {
            "past_events": p_events,
            "quantity": len(p_events)
        })