from kb import SeeedBoard
from kmk.keys import KC
from kmk.handlers.sequences import send_string
from kmk.extensions.RGB import RGB
from kmk.modules.layers import Layers
from kmk.modules.midi import MidiKeys

keyboard = SeeedBoard()

rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels, hue_default=0, sat_default=255, val_default=255)
keyboard.extensions = [rgb_ext]
keyboard.modules = [Layers(), MidiKeys()]

keyboard.keymap = [

    [KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
	KC.AUDIO_VOL_DOWN, KC.X, KC.AUDIO_VOL_DOWN,
	KC.A, KC.B, KC.MO(1)

    ],

    [KC.RGB_HUI, KC.RGB_SAI, KC.RGB_VAI,
	KC.RGB_HUD, KC.RGB_SAD, KC.RGB_VAD,
	KC.RGB_MODE_PLAIN, KC.RGB_MODE_SWIRL, KC.NO

    ],

    [KC.N1, KC.N2, KC.N3,
	KC.N4, KC.N5, KC.N6,
	KC.N7, KC.MO(0), KC.N9

    ],

    [KC.N1, KC.N2, KC.N3,
	KC.N4, KC.N5, KC.N6,
	KC.N7, KC.N8, KC.N9

    ]
]

if __name__ == '__main__': keyboard.go()

