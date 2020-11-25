from typing import Dict, Literal, Optional, Sequence

from graphviz import Digraph

from timeline.event import Event


def graph_timeline(
    events: Sequence[Event], fill_dict: Optional[Dict[str, str]] = None,
) -> Digraph:
    """ Produces Graphviz representation of timeline sequence

    Blue nodes are cooking, orange nodes are prep, gray is boring,
    and pink is fun

    Parameters
    ----------
    events: Sequence[Event]
        time ordered sequence of events
    fill_dict: Optional[Dict[str,str]]
        dictionary w/ key `event_type` and value `fillcolor` to be used for
        graph background, unspecified `event_type`, `fillcolor` pairs
        default to gray

    Returns
    -------
    dot: Digraph
        graph of timeline
    """
    if not fill_dict:
        fill_dict = {"cooking": "orange", "prep": "lightblue", "fun": "pink"}

    node_attr = dict(
        style="filled",
        shape="box",
        align="left",
        fontsize="12",
        ranksep="0.1",
        height="0.2",
    )

    dot = Digraph(node_attr=node_attr, graph_attr=dict(size="12,12"))

    for i, event in enumerate(events):
        if event.event_type:
            fillcolor = fill_dict.get(event.event_type)
        else:
            fillcolor = None

        notes = f"\n Notes: {event.notes}" if event.notes else ""
        description = f"{event.name.upper()}\n{event.event_time}{notes}"
        if i == (len(events) - 1):
            dot.node(str(i), description, fillcolor=fillcolor)
        else:
            dot.node(str(i), description, fillcolor=fillcolor)
            dot.edge(str(i), str(i + 1))

    return dot
