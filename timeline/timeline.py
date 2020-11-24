from datetime import datetime, timedelta
from typing import Sequence

from timeline.event import Event


def timeline(
    event_time: datetime, events: Sequence[Event], verbose: bool = True
) -> Sequence[Event]:
    """construct timeline based on specified event durations

    Parameters
    ----------
    event_time: datetime
        time event takes place
    events: Sequence[Event]
        time ordered sequence of events
    verbose: bool, default = False
        print timeline to stdout

    Returns
    -------
    events: Sequence[Event]
        time ordered sequence of events w.r.t. `event_time`
    """
    temp_time = timedelta(seconds=0)
    for event in reversed(events):
        temp_time += event.duration
        event._event_time = event_time - temp_time

    if verbose:
        for event in events:
            notes = f" - Notes: {event.notes}" if event.notes else ""
            print(f"{event._event_time} {event.name}{notes}")

    return events
