from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Literal, Optional


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
    event_type: Optional, one of "cooking", "prep", "fun", default=None
        type of event; used to graph fill colors
    """

    name: str
    duration: timedelta
    notes: Optional[str] = None
    event_type: Optional[Literal["cooking", "prep", "fun"]] = None
    event_time: Optional[datetime] = None
