import gc
import board
import os
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import adafruit_imageload

from kmk.extensions import Extension

class LcdDisplayMode:
    TXT = 0
    IMG = 1


class LcdReactionType:
    STATIC = 0
    LAYER = 1


class LcdData:
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


class Lcd(Extension):
    def __init__(
        self,
        views,
        oWidth=80,
        oHeight=160,
        flip: bool = False,
    ):
        displayio.release_displays()
        self.rotation = 180 if flip else 0
        self._views = views.data
        self._width = oWidth
        self._height = oHeight
        self._prevLayers = 0
        self.splash = displayio.Group()
        
        self.odb1 = displayio.OnDiskBitmap('/1.bmp')
        self.odb2 = displayio.OnDiskBitmap('/2.bmp')
        self.odb3 = displayio.OnDiskBitmap('/3.bmp')
        self.odb4 = displayio.OnDiskBitmap('/4.bmp')
        
        self.layerImages = [self.odb1, self.odb2, self.odb3, self.odb4]
        
        self.bg_img = displayio.TileGrid(bitmap=self.layerImages[1], pixel_shader=self.layerImages[1].pixel_shader)
        self.splash.append(self.bg_img)
        
        self.layerLabel = label.Label(terminalio.FONT, text="XXXX", color=0xFFFFFF, x=15, y=10)
        self.splash.append(self.layerLabel)
        
        
        gc.collect()

    def renderText(self, layer, singleView):
        # for now we only have static things and react to layers. But when we react to battery % and wpm we can handle the logic here
        if singleView[0] == LcdReactionType.STATIC:
            return singleView[1][0]
        if singleView[0] == LcdReactionType.LAYER:
            return singleView[1][layer]


    def renderLcdImgLayer(self, layer):
        
        
        #self.bg_img = displayio.TileGrid(bitmap=self.layerImages[layer], pixel_shader=self.layerImages[layer].pixel_shader)
        #self.splash[0] = (self.bg_img)
       
        
        self.layerLabel.text = self.renderText(layer, self._views[1])
        self.splash[1] = (self.layerLabel)
        gc.collect()
        
    def updateLCD(self, sandbox):
        self.renderLcdImgLayer(sandbox.active_layers[0])
        gc.collect()

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, keyboard):
        displayio.release_displays()
        spi = board.SPI()
        tft_cs = board.D7
        tft_dc = board.D0
        displayio.release_displays()
        display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, baudrate=60000000)
        self._display = ST7735R(display_bus, width=80, height=160, colstart=26, rowstart=1, invert=True)
        self.layerLabel.text = self.renderText(0, self._views[1])
        self._display.show(self.splash)
        gc.collect()
        return

    def before_matrix_scan(self, sandbox):
        return


    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        if sandbox.active_layers[0] != self._prevLayers:
            self._prevLayers = sandbox.active_layers[0]
            self.updateLCD(sandbox)
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
