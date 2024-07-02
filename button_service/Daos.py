from .button_conn import ButtonConnection
from .db_conn import DBConnection, InsertIntoButtonStatusTbl
import json


class ButtonRead:
    def __init__(self, conn: ButtonConnection):
        self._conn = conn

    def read(self) -> bool:
        return self._conn.is_pressed()


class ButtonWrite:

    def __init__(self, conn: DBConnection):
        self._db = conn

    def write(self, state, check_time):
        try:
            self._db.execute(
                InsertIntoButtonStatusTbl(
                    state,
                    check_time
                )
            )
            return True
        except Exception as e:
            print(e)
            return False
