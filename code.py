import board
import busio
import adafruit_us100
import time
from adafruit_circuitplayground import cp

# neopixels
cp.pixels.brightness = 0.05
pixel_off_state = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# set up wave gesture
uart = busio.UART(board.TX, board.RX, baudrate=9600)
us100 = adafruit_us100.US100(uart)
wave_list = []

# breaktime flag
breaktime = False


while True:
    while breaktime == False:
        # start the countdown
        cp.pixels.fill(red)
        time_scaled = 10 / 10

        # countdown
        for p in range(10):
            time.sleep(time_scaled)
            cp.pixels[p] = (0, 0, 0)

        #wave gesture
        wave_list = []
        for i in range(0,10):
            distance = us100.distance
            print(distance)
            wave_list.append(distance)
            if distance < 30:
                breaktime = False
            time.sleep(0.2)
            
        wave_list.sort()
        print(wave_list)
        if wave_list[1] > 30:
            breaktime = True


    while breaktime == True:
        #start breaktime
        cp.pixels.fill(green)

        breaktime_scaled = 5 / 10

        # countdown
        for p in range(10):
            time.sleep(breaktime_scaled)
            cp.pixels[p] = (0, 0, 0)

        breaktime = False




