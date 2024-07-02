import os

from .button import ButtonRead, ButtonWrite
from .connection import KeyboardConnection
from .db_conn import CassandraConnection

btnconn = KeyboardConnection('p')
btnR = ButtonRead(
    btnconn
)

dbconn = CassandraConnection()
btnW = ButtonWrite(dbconn)

if __name__ == "__main__":
    while True:
        try:
            status = btnR.read()
            if not btnW.write(status):
                print("data dropped...")
        except KeyboardInterrupt:
            print("Interrupted! Stopping!")
            break
