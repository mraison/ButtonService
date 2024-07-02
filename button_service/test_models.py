import time
from unittest.mock import MagicMock

from .Models import ButtonStatusModel
from .Daos import ButtonWrite
from .db_conn import DBConnection


def test_button_status_serialize():
    t = 12345
    time.time = MagicMock(return_value=t)

    db = DBConnection
    db.execute = MagicMock(return_value=True)
    btn = ButtonWrite(db)

    status = ButtonStatusModel(True, btn)
    expected = '{"state": true, "check_time": %s}' % t

    assert expected == status.serialize()


def test_button_status_update():
    t = 12345
    time.time = MagicMock(return_value=t)

    db = DBConnection
    db.execute = MagicMock(return_value=True)
    btn = ButtonWrite(db)

    status = ButtonStatusModel(True, btn)

    assert status.state
    assert status.check_time == t

    time.time = MagicMock(return_value=t+1)

    status.update(False)

    assert not status.state
    assert status.check_time == t + 1
