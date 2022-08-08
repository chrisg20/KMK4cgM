# KMK4cgM
A guide for using KMK on cgMacropads.


# Editing

To put the macropad into editor mode, unplug the device, then hold down the center key and plug it into your computer.

A CIRCUITPY drive will show up like a USB flash drive in your file explorer. Locate the file main.py.

Right click on main.py and select Open With, then choose a raw text editor like Notepad, or TextEdit on Mac.

The file should open and look like this:


`from kb import SeeedBoard, send_string
from kmk.keys import KC
keyboard = SeeedBoard()

keyboard.keymap = [

    [KC.NUMPAD_1, KC.NUMPAD_2, KC.NUMPAD_3,
     KC.NUMPAD_4, KC.NUMPAD_5, KC.NUMPAD_6,
     KC.NUMPAD_7, KC.NUMPAD_8, KC.NUMPAD_9,
     
     ]
]

`if __name__ == '__main__': keyboard.go()


The 3x3 section of key codes in the middle determines the layout of the board. By changing these codes, the keys can be made to perform whatever function you like!

This file is a Python program, so it is possible to make errors which prevent things from working. If this happens and you can't fix the error, don't worry! Just download the main.py and kb.py from here and replace the broken files. It is important to leave the names main.py and kb.py as they are.

# Keys

The codes for basic keys are very simple-- just `KC.` followed by the key code. Note that it must be all caps. This does not result in a capital letter being typed-- that is done with a simultaneous shift key press which is shown in the next section.

Here is an example of a key map of the letters A to I:


`    [KC.A, KC.B, KC.C,
     KC.D, KC.E, KC.F,
     KC.G, KC.H, KC.I,
     ]`


Number keys must be preceded with an N, so use `KC.N1`, `KC.N2`, and so on.

Symbols must be typed out fully. For example, `KC.\` will not work. `KC.BACKSLASH` will.

A complete list of codes can be found here: http://kmkfw.io/docs/keycodes.

# Key Combos

# Key Sequences

# Media controls

# LED commands

# MIDI commands

# Full KMK Reinstall
All cgMacropads come preinstalled with KMK firmware and work out of the box. Jump down to the customization section to learn how to edit the keymap. 

To reinstall KMK from the beginning, first put the macropad into editor mode by holding down the four corner keys and plugging it into your computer.

A CIRCUITPY drive will show up like a USB flash drive in your file explorer. Find it and delete all its contents.

Next, download the base KMK firmware here.

Unzip it and copy ONLY the KMK folder and the boot.py file onto the USB drive corresponding to your board (often appearing as CIRCUITPY)
