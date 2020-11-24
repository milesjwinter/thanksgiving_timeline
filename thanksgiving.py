from datetime import datetime, timedelta

from timeline import Event, graph_timeline, timeline

events = [
    Event(name="Leave Chicago", duration=timedelta(hours=1, minutes=30)),
    Event(name="Settle in", duration=timedelta(minutes=15)),
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
        duration=timedelta(minutes=45),
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
        name="Sides in", duration=timedelta(minutes=25), event_type="cooking"
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


dinner_time = datetime(2020, 11, 26, hour=14)
events = timeline(event_time=dinner_time, events=events)
g = graph_timeline(events)
g.view()
