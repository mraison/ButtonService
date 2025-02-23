import time
from unittest.mock import MagicMock

from button_service.models import ButtonStatusModel
from button_service.daos import StatusDao
from button_service.db_conn import DBConnection


def test_button_status_serialize():
    t = 12345
    time.time = MagicMock(return_value=t)

    db = DBConnection
    db.execute = MagicMock(return_value=True)
    btn = StatusDao(db)

    status = ButtonStatusModel(1, True, btn)
    expected = '{"device_id": 1, "state": true, "check_time": %s}' % t

    assert expected == status.serialize()


def test_button_status_update():
    t = 12345
    time.time = MagicMock(return_value=t)

    db = DBConnection
    db.execute = MagicMock(return_value=True)
    btn = StatusDao(db)

    status = ButtonStatusModel(1, True, btn)

    assert status.state
    assert status.check_time == t

    time.time = MagicMock(return_value=t+1)

    status.update(False)

    assert not status.state
    assert status.check_time == t + 1
