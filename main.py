print("Starting")

from kb import SeeedBoard
from kmk.keys import KC

keyboard = SeeedBoard()

keyboard.keymap = [
    [KC.RGB_TOG, KC.RGB_HUD, KC.RGB_HUI,
     KC.RGB_VAI, KC.RGB_VAD, KC.RGB_MODE_SWIRL,
     KC.RGB_ANI, KC.RGB_AND, KC.RGB_MODE_KNIGHT,
     
     
     
     ]
]

# keyboard.keymap = [
#     [KC.NUMPAD_1, KC.NUMPAD_2, KC.NUMPAD_3,
#      KC.NUMPAD_4, KC.NUMPAD_5, KC.NUMPAD_6,
#      KC.NUMPAD_7, KC.NUMPAD_8, KC.NUMPAD_9,
#      
#      
#      
#      ]
# ]

if __name__ == '__main__':
    keyboard.go()