from kombu import Exchange
import os
from dotenv import load_dotenv

load_dotenv()

from button_service.daos import StatusDao
from button_service.client import RabbitClient
from button_service.models import ButtonStatusModel
from button_service.button_conn import KeyboardConnection
from button_service.db_conn import CassandraConnection

btnconn = KeyboardConnection('p')

dbconn = CassandraConnection(
    os.environ.get('CASSANDRA_IP', '127.0.0.1'),
    int(os.environ.get('CASSANDRA_PORT', '9042'))
)
btnW = StatusDao(dbconn)

rab_conn = RabbitClient(
    os.environ.get('AMQP_URL', ''),
    'panic_key',
    Exchange('panic_ex', type='direct')
)

if __name__ == "__main__":
    status = ButtonStatusModel(
        int(os.environ.get('DEVICE_ID', '-1')),
        False,
        btnW,
        rab_conn,
    )

    print("Ready!")
    while True:
        try:
            if btnconn.is_pressed():
                status.update(not status.state)
                if not status.save():
                    print("data dropped...")
                # # I need to wait until the button is released again to continue the original while loop...
                # while button.is_pressed():
                #     pass

        except KeyboardInterrupt:
            print("Interrupted! Stopping!")
            break
