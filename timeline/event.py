from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional


@dataclass
class Event:
    """event definition

    parameters
    ----------
    name: str
        name of event
    duration: timedelta
        time until next timeline event (not full event duration)
    notes: str, default=None
        optional event notes
    event_type: Optional[str], default=None
        type of event; used to graph fill colors (see timeline.utils.py)
    event_time: Optional[datetime], default=None
        time of event
    """

    name: str
    duration: timedelta
    notes: Optional[str] = None
    event_type: Optional[str] = None
    event_time: Optional[datetime] = None
