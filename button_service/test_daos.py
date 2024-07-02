import time

from .button_conn import ButtonConnection
from .Daos import ButtonRead, ButtonWrite
from .db_conn import DBConnection
from unittest.mock import MagicMock


def test_button_is_pressed():
    conn = ButtonConnection
    conn.is_pressed = MagicMock(return_value=True)

    btn = ButtonRead(conn)

    assert btn.read()


def test_button_is_not_pressed():
    conn = ButtonConnection
    conn.is_pressed = MagicMock(return_value=False)

    btn = ButtonRead(conn)

    assert not btn.read()


def test_button_status_write():
    db = DBConnection
    db.execute = MagicMock(return_value=True)

    btn = ButtonWrite(db)

    t = time.time()

    assert btn.write(True, t)
    db.execute.assert_called()
