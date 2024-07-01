from .connection import ButtonConnection
import json
import time


class ButtonStatus:
    def __init__(self, state, change_time, check_time):
        self.state = state
        self.change_time = change_time
        self.check_time = check_time

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
                change_time=self.change_time,
                check_time=self.change_time
            )
        else:
            # update only the time last checked and return.
            return ButtonStatus(
                state=self.status,
                change_time=self.change_time,
                check_time=time.time()
            )