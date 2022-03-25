import pytest
from qtpy import PYQT5, PYSIDE2

@pytest.mark.skipif(not (PYQT5 or PYSIDE2), reason="Only available in Qt5 bindings")
def test_qtpositioning():
    """Test the qtpy.QtPositioning namespace"""
    from qtpy import QtPositioning
    assert QtPositioning.QGeoAddress is not None
    assert QtPositioning.QGeoAreaMonitorInfo is not None
    assert QtPositioning.QGeoAreaMonitorSource is not None
    assert QtPositioning.QGeoCircle is not None
    assert QtPositioning.QGeoCoordinate is not None
    assert QtPositioning.QGeoLocation is not None
    assert QtPositioning.QGeoPath is not None
    # CI for 3.7 uses Qt 5.9
    # assert QtPositioning.QGeoPolygon is not None  # New in Qt 5.10
    assert QtPositioning.QGeoPositionInfo is not None
    assert QtPositioning.QGeoPositionInfoSource is not None
    # QGeoPositionInfoSourceFactory is not available in PyQt
    # assert QtPositioning.QGeoPositionInfoSourceFactory is not None  # New in Qt 5.2
    # assert QtPositioning.QGeoPositionInfoSourceFactoryV2 is not None  # New in Qt 5.14
    assert QtPositioning.QGeoRectangle is not None
    assert QtPositioning.QGeoSatelliteInfo is not None
    assert QtPositioning.QGeoSatelliteInfoSource is not None
    assert QtPositioning.QGeoShape is not None
    assert QtPositioning.QNmeaPositionInfoSource is not None
