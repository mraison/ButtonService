import keyboard


class ButtonConnectionException(Exception):
    pass


class InvalidButtonTypeException(ButtonConnectionException):
    pass


class ButtonConnection:
    def is_pressed(self) -> bool:
        pass


class KeyboardConnection(ButtonConnection):
    def __init__(self, panicKey = 'p'):
        super().__init__()
        self._panicKey = panicKey

    def is_pressed(self) -> bool:
        return keyboard.is_pressed(self._panicKey)


class GPIOConnection(ButtonConnection):
    # implement this later...
    pass


KEYBOARD_BUTTON = 0
GPIO_BUTTON = 1

BUTTON_TYPE_MAP = {
    KEYBOARD_BUTTON: KeyboardConnection,
    GPIO_BUTTON: GPIOConnection
}


def getButtonConn(button_type) -> ButtonConnection:
    if button_type not in BUTTON_TYPE_MAP:
        raise InvalidButtonTypeException(f"{button_type} is not a valid button connection option.")

    return BUTTON_TYPE_MAP[button_type]()
