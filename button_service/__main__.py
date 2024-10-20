import time

from .daos import ButtonDao, StatusDao
from .models import ButtonStatusModel, ButtonModel
from .button_conn import KeyboardConnection
from .db_conn import CassandraConnection

btnconn = KeyboardConnection('p')
btnR = ButtonDao(
    btnconn
)

dbconn = CassandraConnection()
btnW = StatusDao(dbconn)

if __name__ == "__main__":
    status = ButtonStatusModel(False, btnW)
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
