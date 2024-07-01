import time

from connection import ButtonConnection
from button import ButtonStatus, ButtonRead
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
