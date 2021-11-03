import board
import busio
import adafruit_us100
import time
from adafruit_circuitplayground import cp

# set up wave gesture
uart = busio.UART(board.TX, board.RX, baudrate=9600)
us100 = adafruit_us100.US100(uart)
max_distance = 12

breaktime = False

while True:
    while breaktime == False:
        # Turn ON all the NeoPixels
        cp.pixels.fill((255, 255, 255))

        # Compute DT
        DT = 5 / 10

        # Turn OFF the NeoPixels one at a time, waiting DT each time
        for p in range(10):
            time.sleep(DT)
            cp.pixels[p] = (0, 0, 0)



        # Wait for wave to reset timer
        while not breaktime == True:
            #wave gesture
            distance = us100.distance
            print(distance)
            time.sleep(0.5)
            if distance < 30:
                breaktime = False
            elif distance > 30:
                breaktime = True

    while breaktime == True:
        # Turn ON all the NeoPixels
        cp.pixels.fill((255, 255, 0))

        # Compute DT
        DT = 5 / 10

        # Turn OFF the NeoPixels one at a time, waiting DT each time
        for p in range(10):
            time.sleep(DT)
            cp.pixels[p] = (0, 0, 0)

        breaktime = False



