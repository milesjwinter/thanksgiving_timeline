from datetime import datetime, timedelta

from timeline import Event, graph_timeline, timeline

events = [
    Event(
        name="Prep Turkey",
        duration=timedelta(minutes=35),
        notes="oven at 400",
        event_type="prep",
    ),
    Event(
        name="Turkey in",
        duration=timedelta(minutes=45),
        notes="breast down",
        event_type="cooking",
    ),
    Event(
        name="Flip Turkey",
        duration=timedelta(minutes=5),
        notes="breast up",
        event_type="cooking",
    ),
    Event(
        name="Turkey Back in",
        duration=timedelta(hours=1, minutes=20),
        event_type="cooking",
    ),
    Event(
        name="Prep Stuffing",
        duration=timedelta(minutes=15),
        notes="AL foil on",
        event_type="prep",
    ),
    Event(
        name="Turkey out",
        duration=timedelta(minutes=5),
        notes="adjust racks, cover turkey",
        event_type="cooking",
    ),
    Event(
        name="Stuffing in", duration=timedelta(minutes=10), event_type="cooking"
    ),
    Event(
        name="GB casserole in",
        duration=timedelta(minutes=10),
        event_type="cooking",
    ),
    Event(
        name="Uncover stuffing",
        duration=timedelta(minutes=5),
        notes="add topping to GB casserole",
        event_type="cooking",
    ),
    Event(
        name="Carve Turkey", duration=timedelta(minutes=15), event_type="prep"
    ),
    Event(name="Dinner time", duration=timedelta(minutes=0), event_type="fun"),
]


dinner_time = datetime(2021, 11, 25, hour=17, minute=30)
events = timeline(events=events, event_time=dinner_time, event_time_type="end")
g = graph_timeline(events)
g.format = "png"
g.render("outputs/timeline-graph.gv", view=False)
