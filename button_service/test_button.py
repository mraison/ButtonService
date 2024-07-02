import time

from .connection import ButtonConnection
from .button import ButtonStatus, ButtonRead, ButtonWrite
from .db_conn import DBConnection
from unittest.mock import MagicMock

def test_button_is_pressed():
    conn = ButtonConnection
    conn.is_pressed = MagicMock(return_value=True)

    btn = ButtonRead(conn)

    status = btn.read()

    assert status.state
    assert status.change_time == status.check_time


def test_button_is_not_pressed():
    conn = ButtonConnection
    conn.is_pressed = MagicMock(return_value=False)

    btn = ButtonRead(conn)

    status = btn.read()

    assert not status.state


def test_button_status_serialize():
    t = time.time()
    status = ButtonStatus(True, t, t)
    expected = '{"state": true, "change_time": %s, "check_time": %s}' % (t, t)

    assert expected == status.serialize()


def test_button_status_write():
    db = DBConnection
    db.execute = MagicMock(return_value=True)

    btn = ButtonWrite(db)

    t = time.time()

    assert btn.write(ButtonStatus(True, t, t))
    db.execute.assert_called()


def test_button_status_no_write():
    db = DBConnection
    db.execute = MagicMock(return_value=True)

    btn = ButtonWrite(db)

    t = time.time()

    assert btn.write(ButtonStatus(True, t, t+5))
    db.execute.assert_not_called()
