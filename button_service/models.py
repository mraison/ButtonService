import json
import time

from .daos import StatusDao, ButtonDao
from .client import RabbitClient


class ButtonStatusModel:
    device_id = 1

    def __init__(self, state: bool, dao: StatusDao, rabbit_cli: RabbitClient = None):
        self.state = state
        self.check_time = int(time.time())
        self._dao = dao
        self._rabbit_cli = rabbit_cli

    def save(self):
        resp = self._dao.write(self.device_id, self.state, self.check_time)
        if resp and self._rabbit_cli:
            return self._rabbit_cli.send(self.to_dict())
        else:
            return resp

    def update(self, state):
        self.state = state
        self.check_time = int(time.time())

    def serialize(self) -> str:
        return json.dumps(
            self.to_dict()
        )

    def to_dict(self):
        return {
            'device_id': self.device_id,
            'state': self.state,
            'check_time': self.check_time
        }


class ButtonModel:
    def __init__(self, dao: ButtonDao):
        self._dao = dao

    def is_pressed(self):
        return self._dao.read()
