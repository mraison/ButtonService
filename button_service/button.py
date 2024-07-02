from .connection import ButtonConnection
from .db_conn import DBConnection, InsertIntoButtonStatusTbl
import json
import time


class ButtonStatus:
    def __init__(self, state, change_time, check_time):
        self.state = state
        self.change_time = change_time
        self.check_time = check_time

    @property
    def is_new_state(self):
        return self.change_time == self.check_time

    def serialize(self) -> str:
        return json.dumps(
            {
                'state': self.state,
                'change_time': self.change_time,
                'check_time': self.check_time
            }
        )


class ButtonRead:
    def __init__(self, conn: ButtonConnection):
        self._conn = conn
        self.status = False
        self.change_time = time.time()

    def read(self) -> ButtonStatus:
        if self._conn.is_pressed():
            # toggle on button press
            self.status = not self.status
            # update time last changed
            self.change_time = time.time()

            # time checked is same as last changed now.
            return ButtonStatus(
                state=self.status,
                change_time=int(self.change_time),
                check_time=int(self.change_time)
            )
        else:
            # update only the time last checked and return.
            return ButtonStatus(
                state=self.status,
                change_time=int(self.change_time),
                check_time=int(time.time())
            )


class ButtonWrite:

    def __init__(self, conn: DBConnection):
        self._db = conn

    def write(self, button_status: ButtonStatus):
        if button_status.is_new_state:
            try:
                self._db.execute(
                    InsertIntoButtonStatusTbl(
                        button_status.state,
                        button_status.change_time
                    )
                )
                return True
            except Exception as e:
                print(e)
                return False

        return True
