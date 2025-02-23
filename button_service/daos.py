from button_service.db_conn import DBConnection, InsertIntoButtonStatusTbl
import json


class StatusDao:

    def __init__(self, conn: DBConnection):
        self._db = conn

    def write(self, device_id, state, check_time):
        try:
            self._db.execute(
                InsertIntoButtonStatusTbl(
                    device_id,
                    state,
                    check_time
                )
            )
            return True
        except Exception as e:
            print(e)
            return False
