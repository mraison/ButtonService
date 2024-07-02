import time

from .Daos import ButtonRead, ButtonWrite
from .Models import ButtonStatusModel
from .button_conn import KeyboardConnection
from .db_conn import CassandraConnection

btnconn = KeyboardConnection('p')
btnR = ButtonRead(
    btnconn
)

dbconn = CassandraConnection()
btnW = ButtonWrite(dbconn)

if __name__ == "__main__":
    status = ButtonStatusModel(False, btnW)

    print("Ready!")
    while True:
        try:
            if btnR.read():
                status.update(not status.state)
                if not status.save():
                    print("data dropped...")
                # I need to wait until the button is released again to continue the original while loop...
                while btnR.read():
                    pass

        except KeyboardInterrupt:
            print("Interrupted! Stopping!")
            break
