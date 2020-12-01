import argparse
from ws2812b_neopixel_luma_led_matrix.neopixel_demo import show_effect

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Input effects for ws2812b/neopixel")
    parser.add_argument('effect', type=str, help="Input Effect Type")
    effect = parser.parse_args()
    print(f"Received command line effect argument : {effect}")
    show_effect(effect);