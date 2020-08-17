import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90,
                     rotate=0, blocks_arranged_in_reverse_order=False)

    show_welcome(device)

    show_vertical_message(device)

    show_header(device)

def show_header(device):
    while True:
        with canvas(device) as draw:
            text(draw, (0, 0), "donsky", fill="white", font=proportional(LCD_FONT))

def show_vertical_message(device):
    words = [
        "Hello", "IOT", "World!", " "
    ]
    virtual = viewport(device, width=device.width, height=len(words) * 8)
    with canvas(virtual) as draw:
        for i, word in enumerate(words):
            text(draw, (0, i * 8), word, fill="white", font=proportional(SINCLAIR_FONT))
    for i in range(virtual.height - device.height):
        virtual.set_position((0, i))
        time.sleep(0.20)


def show_welcome(device):
    msg = "Welcome to Donsky Tech"
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

