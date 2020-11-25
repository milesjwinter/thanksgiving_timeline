from datetime import datetime, timedelta
from typing import Literal, Sequence

from timeline.event import Event


def timeline(
    events: Sequence[Event],
    event_time: datetime,
    event_time_type: Literal["start", "end"] = "end",
    verbose: bool = True,
) -> Sequence[Event]:
    """construct timeline based on specified event durations. Only
    useful when you don't know the absolute event times. Note: this
    function assigns the `event_time` attribute of the input event
    sequence

    Parameters
    ----------
    events: Sequence[Event]
        time ordered sequence of events leading up to `event_time`
    event_time: datetime
        time event takes place
    event_time_type: str, one of "start" or "end", default = "end"
        literal indicating whether `event_time` is at the beginning of the
        sequence or the end. For example, "start" should be used to answer
        the question, if I start prep at `event_time` when will dinner be?
        Similarly, "end" should be used to answer the question, if I want to
        eat dinner at `event_time` when should I begin prep/cooking
    verbose: bool, default = True
        print timeline to stdout

    Returns
    -------
    events: Sequence[Event]
        time ordered sequence of events w.r.t. `event_time`

    Raises
    ------
    AssertionError
    """
    assert event_time_type in [
        "start",
        "end",
    ], "event_time_type must be 'start' or 'end'"

    temp_time = timedelta(seconds=0)
    if event_time_type == "end":
        for event in reversed(events):
            temp_time += event.duration
            event.event_time = event_time - temp_time

    if event_time_type == "start":
        for event in events:
            temp_time += event.duration
            event.event_time = event_time + temp_time

    if verbose:
        for event in events:
            notes = f" - Notes: {event.notes}" if event.notes else ""
            print(f"{event.event_time} {event.name}{notes}")

    return events
