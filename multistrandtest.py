import time
from rpi_ws281x import *


strip1 = PixelStrip(120, 18, brightness=65, channel=0)
strip2 = PixelStrip(120, 21, brightness=65, channel=0)

# Define functions which animate LEDs in various ways.
def colorWipeForward(color, wait_ms=100):
    for i in range(120):
        if i == 0:
            strip1.setPixelColor(119, Color(0,0,0))
            strip2.setPixelColor(119, Color(0,0,0))
        else:
            strip1.setPixelColor(i-1, Color(0,0,0))
            strip2.setPixelColor(i-1, Color(0,0,0))
        strip1.setPixelColor(i, color)
        strip1.show()
        strip2.setPixelColor(i, color)
        strip2.show()
        time.sleep(wait_ms/1000.0)


def colorWipeReverse(color, wait_ms=100):
    for i in reversed(range(120)):
        if i == 119:
            strip1.setPixelColor(0, Color(0,0,0))
            strip2.setPixelColor(0, Color(0,0,0))
        else:
            strip1.setPixelColor(i+1, Color(0,0,0))
            strip2.setPixelColor(i+1, Color(0,0,0))
        strip1.setPixelColor(i, color)
        strip1.show()

        strip2.setPixelColor(i, color)
        strip2.show()
        time.sleep(wait_ms/1000.0)


def colorAll(strip, wait_ms=200):
    for i in range(strip.numPixels()):
        color = Color(255,255,255)
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000.0)


def colorWipeAll():
    for i in range(120):
        strip1.setPixelColor(i, Color(0,0,0))
        strip2.setPixelColor(i, Color(0,0,0))
    strip1.show()
    strip2.show()


# Main program logic follows:
if __name__ == '__main__':

    strip1.begin()
    strip2.begin()

    try:
        while True:
            colorWipeForward(Color(255,255,255), 4)
            colorWipeReverse(Color(255,255,255), 4)
            #colorAll(strip)

    finally:
        colorWipeAll()