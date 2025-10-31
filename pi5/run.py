from rpi5_ws2812.ws2812 import Color, WS2812SpiDriver
import time

LED_MAX_SIZE = 120

# Define functions which animate LEDs in various ways.
def colorWipeForward(strip, color, wait_ms=100):
    for i in range(LED_MAX_SIZE):
        if i == 0:
            strip.set_pixel_color(LED_MAX_SIZE-1, Color(0,0,0))
        else:
            strip.set_pixel_color(i-1, Color(0,0,0))
        strip.set_pixel_color(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorWipeReverse(strip, color, wait_ms=100):
    for i in reversed(range(LED_MAX_SIZE)):
        if i == LED_MAX_SIZE-1:
            strip.set_pixel_color(0, Color(0,0,0))
        else:
            strip.set_pixel_color(i+1, Color(0,0,0))
        strip.set_pixel_color(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorAll(strip, wait_ms=200):
    for i in range(LED_MAX_SIZE):
        color = Color(255,255,255)
        strip.set_pixel_color(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)


def colorWipeAll(strip):
    for i in range(LED_MAX_SIZE):
        strip.set_pixel_color(i, Color(0,0,0))
    strip.show()

if __name__ == "__main__":

    # Initialize the WS2812 strip with 100 leds and SPI channel 0, CE0
    strip = WS2812SpiDriver(spi_bus=0, spi_device=0, led_count=LED_MAX_SIZE).get_strip()

    try:
        while True:
            colorWipeForward(strip, Color(255,255,255), 4)
            colorWipeReverse(strip, Color(255,255,255), 4)
            #colorAll(strip)

    finally:
        colorWipeAll(strip)