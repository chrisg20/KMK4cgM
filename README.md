<img src="https://i.etsystatic.com/36617648/r/il/2a4033/4527146603/il_1588xN.4527146603_4m6o.jpg" width="400">


# KMK4cgM
A guide for using KMK on cgMacropads, currently sold on Etsy [here](https://www.etsy.com/shop/cgMacropads)!

# LK-33i
If you have the newer LK-33i with the knob and LCD screen, click [here](https://www.etsy.com/shop/cgMacropads)!

<img src="https://i.etsystatic.com/36617648/r/il/9dfb82/4751558020/il_794xN.4751558020_27wn.jpg" width="400">

# IMPORTANT
If your device is not recognized in cgEditor, ensure the device is visible as a usb drive (hold center key while plugging in) and is renamed to CGM-33 instead of CIRCUITPY.

# Editing with cgEditor

The download for our editing software can be found [here](https://github.com/chrisg20/KMK4cgM/releases/tag/untagged-8f703d914059e1e19318). This is the easiest way to edit the keymaps, and should be sufficient for many users. The software is still very much in beta and feedback is welcome!

IMPORTANT! Before opening the editing software, put the macropad into editor mode. This is done by unplugging the device, then holding down the center key while plugging it into your computer. Hold the key for a few seconds after the device is connected.

A CGM-33 drive will show up like a USB flash drive in your file explorer.

# Editing the code yourself

Locate the file main.py on the CGM-33 drive.

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

Key combos are written as follows: `KC.LCTL(KC.LSFT)`.

This keycode holds down left control and presses left shift. This can be extended further to `KC.LCTL(KC.LSFT(KC.V))`.

This enters the combo: Left CTRL + Left Shift + V.

# Key Sequences

# Media controls

Examples: `KC.AUDIO_MUTE, KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN`. Full list can be found [here](http://kmkfw.io/docs/media_keys).

# LED commands

# MIDI commands

# Full KMK Reinstall

To reinstall KMK from the beginning, first put the macropad into editor mode by holding down the center key and plugging it into your computer.

A CGM-33 drive will show up like a USB flash drive in your file explorer. Find it and delete all its contents.

Next, download the base KMK firmware according to steps 1-3 of the guide [here](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/Getting_Started.md).

Then, copy ONLY the KMK folder and the boot.py file from this page onto the USB drive (appearing as CGM-33).
