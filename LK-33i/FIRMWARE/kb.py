import board
import busio
from digitalio import DigitalInOut, Direction, Pull

from adafruit_mcp230xx.mcp23017 import MCP23017
from kmk.scanners.encoder import RotaryioEncoder

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digitalio import MatrixScanner
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.RGB import RGB


i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=400000)
mcp = MCP23017(i2c, address=0x20)


class SeeedBoard(KMKKeyboard):
    
    rgb_pixel_pin = board.D1
    rgb_num_pixels = 24
    
    def __init__(self):

        self.matrix = [
            
            MatrixScanner(
            cols= [mcp.get_pin(11), mcp.get_pin(12), mcp.get_pin(13)],
            rows= [mcp.get_pin(8), mcp.get_pin(9), mcp.get_pin(10)]),
            
            RotaryioEncoder(
            pin_a=board.D2,
            pin_b=board.D3,
            divisor=8,),
            
            KeysScanner(pins=[board.D6],
            value_when_pressed=False,
            pull=True,
            interval=0.02,
            max_events=64
        )
        ]