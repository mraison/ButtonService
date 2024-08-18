import json
import time

from .Daos import ButtonWrite


class ButtonStatusModel:
    device_id = 1

    def __init__(self, state, button_writter: ButtonWrite):
        self.state = state
        self.check_time = int(time.time())
        self._button_writer = button_writter

    def save(self):
        return self._button_writer.write(self.device_id, self.state, self.check_time)

    def update(self, state):
        self.state = state
        self.check_time = int(time.time())

    def serialize(self) -> str:
        return json.dumps(
            {
                'state': self.state,
                'check_time': self.check_time
            }
        )
