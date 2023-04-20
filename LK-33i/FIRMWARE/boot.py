import supervisor

supervisor.set_next_stack_limit(4096 + 4096)

import storage
import board, digitalio

button = digitalio.DigitalInOut(board.D6)
button.pull = digitalio.Pull.UP

if button.value:
   storage.disable_usb_drive()