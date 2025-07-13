print("Firmware Initialization Startup In Progress... ")

import board
import digitalio
import usb_hid

from kmk.kmk_main import KMKkeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

import displayio
import terminalio
from adafruit_display_text import label
import adafruit_sd1306

print("All Modules Imported")

print("Intializing Display Over I2C...")
displayio.release_displays()
i2c = board.I2C()

dsiplay_width = 128
display_height = 64
display = adafruit_sd1306.SSD1306(i2c, width=dsiplay_width height=display_height)

slpash = displayio.Group()
display.show(splash)

text_area = label.Label(
    terminalio.FONT,
    text="MultiPad Is Starting"
    color=0xFFFFFF,
    x=5
    y=display_height // 2 - 4
)

splash.append(text_area)

multipad = KMKkeyboard()

multipad.col_pins = (board.GP26, board.GP27, board.GP28)
multipad.row_pins = (board.GP0, board.GP29, board.GP01)
multipad.diode_orientation = DiodeOrientation.COL2ROW


multipad.keymap = [
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6
        KC.N1, KC.N2, KC.N3
    ]
]

def update_oled_text(text_to_display):
    text_area.text = text_to_display
    print("Display Update: ", text_to_display)

update_oled_text("MultiPad Ready")

if __name__ == '__main__':
    keyboard.go()
