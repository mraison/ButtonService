from kombu import Exchange
import os

from .daos import ButtonDao, StatusDao
from .client import RabbitClient
from .models import ButtonStatusModel, ButtonModel
from .button_conn import KeyboardConnection
from .db_conn import CassandraConnection

btnconn = KeyboardConnection('p')
btnR = ButtonDao(
    btnconn
)

dbconn = CassandraConnection(
    os.environ.get('CASSANDRA_IP', '127.0.0.1'),
    int(os.environ.get('CASSANDRA_PORT', '9042')
)
btnW = StatusDao(dbconn)

rab_conn = RabbitClient(
    os.environ.get('AMQP_URL', ''),
    'panic_key',
    Exchange('panic_ex', type='direct')
)

if __name__ == "__main__":
    status = ButtonStatusModel(
        int(os.environ.get('DEVICE_ID', '-1')
        False,
        btnW,
        rab_conn,
    )
    button = ButtonModel(btnR)

    print("Ready!")
    while True:
        try:
            if button.is_pressed():
                status.update(not status.state)
                if not status.save():
                    print("data dropped...")
                # I need to wait until the button is released again to continue the original while loop...
                while button.is_pressed():
                    pass

        except KeyboardInterrupt:
            print("Interrupted! Stopping!")
            break
