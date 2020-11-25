from datetime import datetime, timedelta
from typing import Sequence

from timeline.event import Event


def timeline(
    event_time: datetime, events: Sequence[Event], verbose: bool = True
) -> Sequence[Event]:
    """construct timeline based on specified event durations. Most
    useful when you don't know the absolute event times. Events are
    assumed to take place prior to `event_time`

    Parameters
    ----------
    event_time: datetime
        time event takes place
    events: Sequence[Event]
        time ordered sequence of events leading up to `event_time`
    verbose: bool, default = True
        print timeline to stdout

    Returns
    -------
    events: Sequence[Event]
        time ordered sequence of events w.r.t. `event_time`
    """
    temp_time = timedelta(seconds=0)
    for event in reversed(events):
        temp_time += event.duration
        event.event_time = event_time - temp_time

    if verbose:
        for event in events:
            notes = f" - Notes: {event.notes}" if event.notes else ""
            print(f"{event.event_time} {event.name}{notes}")

    return events
