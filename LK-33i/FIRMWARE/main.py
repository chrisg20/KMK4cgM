from kb import SeeedBoard
from kmk.keys import KC
from kmk.handlers.sequences import send_string
from kmk.extensions.RGB import RGB
from kmk.modules.layers import Layers
from kmk.modules.midi import MidiKeys
from kmk.extensions.rgb import AnimationModes
from kmk.extensions.st7735r_lcd import Lcd,LcdDisplayMode,LcdReactionType,LcdData
import board

keyboard = SeeedBoard()

Lcd_ext = Lcd(
    LcdData(
        corner_one={0:LcdReactionType.STATIC,1:["layer"]},
        corner_two={0:LcdReactionType.LAYER,1:["Media","Lighting","Passwords","Numpad"]},
        corner_three={0:LcdReactionType.LAYER,1:["base","raise","lower","adjust"]},
        corner_four={0:LcdReactionType.LAYER,1:["qwerty","nums","shifted","leds"]}
        ))

rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels, hue_default=0, sat_default=0, val_default=200)
keyboard.extensions = [rgb_ext, Lcd_ext]
keyboard.modules = [Layers(), MidiKeys()]

keyboard.debug_enabled = False


keyboard.keymap = [
    


    [KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
	KC.AUDIO_VOL_DOWN, KC.AUDIO_MUTE, KC.AUDIO_VOL_UP,
	KC.MO(3), KC.TO(2), KC.MO(1),
    KC.TO(3), KC.TO(1), KC.AUDIO_MUTE

    ],

    [KC.RGB_HUI, KC.RGB_SAI, KC.RGB_VAI,
	KC.RGB_HUD, KC.RGB_SAD, KC.RGB_VAD,
	KC.RGB_MODE_PLAIN, KC.RGB_MODE_SWIRL, KC.NO,
    KC.TO(0), KC.TO(2), KC.AUDIO_MUTE

    ],
    
    [KC.N1, KC.N2, KC.N3,
	KC.N4, KC.N5, KC.N6,
	KC.N7, KC.TO(0), KC.N9,
    KC.TO(1), KC.TO(3), KC.AUDIO_MUTE

    ],

    [KC.N1, KC.N2, KC.N3,
	KC.N4, KC.N5, KC.N6,
	KC.N7, KC.N8, KC.N9,
    KC.TO(2), KC.TO(0), KC.AUDIO_MUTE

    ]
]


if __name__ == '__main__': keyboard.go()



