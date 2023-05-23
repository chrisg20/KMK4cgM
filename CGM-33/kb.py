import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.RGB import RGB

_KEY_CFG = [
    board.D9, board.D6, board.D3,
    board.D8, board.D5, board.D2,
    board.D7, board.D4, board.D1,
    ]

class SeeedBoard(KMKKeyboard):
    rgb_pixel_pin = board.D0
    rgb_num_pixels = 19
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