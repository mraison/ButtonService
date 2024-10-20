import time

from .button_conn import ButtonConnection
from .daos import StatusDao, ButtonDao
from .db_conn import DBConnection
from unittest.mock import MagicMock


def test_button_is_pressed():
    conn = ButtonConnection
    conn.is_pressed = MagicMock(return_value=True)

    btn = ButtonDao(conn)

    assert btn.read()


def test_button_is_not_pressed():
    conn = ButtonConnection
    conn.is_pressed = MagicMock(return_value=False)

    btn = ButtonDao(conn)

    assert not btn.read()


def test_button_status_write():
    db = DBConnection
    db.execute = MagicMock(return_value=True)

    btn = StatusDao(db)

    t = time.time()

    assert btn.write(2, True, t)
    db.execute.assert_called()
