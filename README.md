# KMK4cgM
A guide for using KMK on cgMacropads.


# Editing

To put the macropad into editor mode, unplug the device, then hold down the four corner keys and plug it into your computer.

A CIRCUITPY drive will show up like a USB flash drive in your file explorer. Locate the file main.py.

Right click on main.py and select Open With, then choose a raw text editor like Notepad, or TextEdit on Mac.

The file should open and look like this:

The 3x3 section of key codes in the middle determines the layout of the board. By changing these codes, the keys can be made to perform whatever function you like!

This file is a Python program, so it is possible to make errors which prevent things from working. If this happens and you can't fix the error, don't worry! Just download the main.py and kb.py from here and replace the broken files. It is important to leave the names main.py and kb.py as they are.

# Keys

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
