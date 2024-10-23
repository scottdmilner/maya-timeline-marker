import logging
from maya import mel

try:
    from PySide6 import QtGui, QtWidgets
except ImportError:
    from PySide2 import QtGui, QtWidgets

from timeline_marker.ui import TimelineMarker
from timeline_marker import utils


log = logging.getLogger(__name__)


def execute():
    """
    Add the timeline marker functionality to Maya's native timeline and
    extend its native menu with actions to manipulate the timeline
    markers.

    :raises RuntimeError: When the timeline marker is already installed.
    """
    # validate timeline marker
    if TimelineMarker.instance is not None:
        raise RuntimeError("timeline-marker has already been installed.")

    # get parent
    parent = utils.get_timeline()
    layout = parent.layout()

    # create layout if non exists
    if layout is None:
        layout = QtWidgets.QVBoxLayout(parent)
        layout.setContentsMargins(0, 0, 0, 0)
        parent.setLayout(layout)

    # create timeline marker
    TimelineMarker.instance = TimelineMarker(parent)
    layout.addWidget(TimelineMarker.instance)

    log.info("timeline-marker installed successfully.")
