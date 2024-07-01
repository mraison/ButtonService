import os

from .button import ButtonRead
from .connection import KeyboardConnection

conn = KeyboardConnection('p')
btn = ButtonRead(
    conn
)
status_file = "button_status"
if __name__ == "__main__":
    while True:
        try:
            status = btn.read()
            if os.path.exists(status_file):
                os.remove(status_file)

            with open(status_file, "w") as f:
                f.write(status.serialize())
        except KeyboardInterrupt:
            print("Interrupted! Stopping!")
            if os.path.exists(status_file):
                os.remove(status_file)
            break
