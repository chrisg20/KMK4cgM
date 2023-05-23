import busio
import gc

import board
from time import sleep
import os
import displayio
import terminalio
import rotaryio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

from kmk.extensions import Extension


class OledDisplayMode:
    TXT = 0
    IMG = 1


class OledReactionType:
    STATIC = 0
    LAYER = 1


class OledData:
    def __init__(
        self,
        image=None,
        corner_one=None,
        corner_two=None,
        corner_three=None,
        corner_four=None,
    ):
        if image:
            self.data = [image]
        elif corner_one and corner_two and corner_three and corner_four:
            self.data = [corner_one, corner_two, corner_three, corner_four]


class Oled(Extension):
    def __init__(
        self,
        views,
        toDisplay=OledDisplayMode.TXT,
        oWidth=80,
        oHeight=160,
        flip: bool = False,
    ):
        displayio.release_displays()
        self.rotation = 180 if flip else 0
        self._views = views.data
        self._toDisplay = toDisplay
        self._width = oWidth
        self._height = oHeight
        self._prevLayers = 0
        gc.collect()

    def returnCurrectRenderText(self, layer, singleView):
        # for now we only have static things and react to layers. But when we react to battery % and wpm we can handle the logic here
        if singleView[0] == OledReactionType.STATIC:
            return singleView[1][0]
        if singleView[0] == OledReactionType.LAYER:
            return singleView[1][layer]

    def renderOledTextLayer(self, layer):
        splash = displayio.Group()
        self._display.show(splash)
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[0]),
                color=0xFFFFFF,
                x=0,
                y=10,
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[1]),
                color=0xFFFFFF,
                x=64,
                y=10,
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[2]),
                color=0xFFFFFF,
                x=0,
                y=25,
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[3]),
                color=0xFFFFFF,
                x=64,
                y=25,
            )
        )
        gc.collect()

    def renderOledImgLayer(self, layer):
        splash = displayio.Group()
        self._display.show(splash)
        odb = displayio.OnDiskBitmap(
            '/' + self.returnCurrectRenderText(layer, self._views[0])
        )
        image = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)
        splash.append(image)
        gc.collect()

    def updateOLED(self, sandbox):
        if self._toDisplay == OledDisplayMode.TXT:
            self.renderOledTextLayer(sandbox.active_layers[0])
        if self._toDisplay == OledDisplayMode.IMG:
            self.renderOledImgLayer(sandbox.active_layers[0])
        gc.collect()

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, board):

        displayio.release_displays()
        spi = board.SPI()
        tft_cs = board.D7
        tft_dc = board.D0
        displayio.release_displays()
        display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
        self._display = ST7735R(display_bus, width=80, height=160, colstart=26, rowstart=1, invert=True)

        if self._toDisplay == OledDisplayMode.TXT:
            self.renderOledTextLayer(0)
        if self._toDisplay == OledDisplayMode.IMG:
            self.renderOledImgLayer(0)
        return

    def before_matrix_scan(self, sandbox):
        if sandbox.active_layers[0] != self._prevLayers:
            self._prevLayers = sandbox.active_layers[0]
            self.updateOLED(sandbox)
        return

    def after_matrix_scan(self, sandbox):

        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
