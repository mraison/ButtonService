import time

from button_service.daos import StatusDao
from button_service.db_conn import DBConnection
from unittest.mock import MagicMock


def test_button_status_write():
    db = DBConnection
    db.execute = MagicMock(return_value=True)

    btn = StatusDao(db)

    t = time.time()

    assert btn.write(2, True, t)
    db.execute.assert_called()
