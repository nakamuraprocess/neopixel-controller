import time
import random
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 120      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 21
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 65     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53

intervalBase = 4
intervalRand = random.randint(0, 20)

# Define functions which animate LEDs in various ways.
def colorWipeForward(strip, color, wait_ms=100):
    for i in range(120):
        if i == 0:
            strip.setPixelColor(119, Color(0,0,0))
        else:
            strip.setPixelColor(i-1, Color(0,0,0))
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorWipeReverse(strip, color, wait_ms=100):
    for i in reversed(range(120)):
        if i == 119:
            strip.setPixelColor(0, Color(0,0,0))
        else:
            strip.setPixelColor(i+1, Color(0,0,0))
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorAll(strip, wait_ms=200):
    for i in range(strip.numPixels()):
        color = Color(255,255,255)
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)


def colorWipeAll(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()


if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    try:
        while True:
            colorWipeForward(strip, Color(255,255,255), intervalBase + intervalRand)
            intervalRand = random.randint(0, 10)
            colorWipeReverse(strip, Color(255,255,255), intervalBase + intervalRand)
            intervalRand = random.randint(0, 10)

    finally:
        colorWipeAll(strip)