import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.RGB import RGB

_KEY_CFG = [
    board.D2, board.D5, board.D6,
    board.D1, board.D4, board.D8,
    board.D0, board.D3, board.D7,
    ]

rgb_ext = RGB(
    pixel_pin=board.D10,
    num_pixels=25,
)

class SeeedBoard(KMKKeyboard):
    extensions = [rgb_ext]
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.02,
            max_events=64
        )