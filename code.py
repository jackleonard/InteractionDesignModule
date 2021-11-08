import board
import busio
import adafruit_us100
import time
from sound import Sound
from adafruit_circuitplayground import cp

# neopixels
cp.pixels.brightness = 0.01
pixel_off_state = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# set up wave gesture
uart = busio.UART(board.TX, board.RX, baudrate=9600)
us100 = adafruit_us100.US100(uart)
wave_list = []

# set up click gesture
mic = Sound() # instance of sound class, no parametres needed

threshold = 100




# breaktime flag
breaktime = False


while True:
    while breaktime == False:
        # start the countdown
        cp.pixels.fill(red)
        time_scaled = 10 / 10 # 10 seconds divided by 10 neopixels

        # countdown
        for p in range(10):
            time.sleep(time_scaled)
            cp.pixels[p] = (0, 0, 0)

        #wave gesture
        wave_list = []
        clap_list = []
        for i in range(0,10):
            mic.record()
            amplitude = mic.sound_level()
            clap_list.append(amplitude)

            distance = us100.distance
            wave_list.append(distance)
            if distance < 30:
                breaktime = False
            time.sleep(0.2)

        clap_list.sort()
        wave_list.sort()
        print(wave_list)
        print(clap_list)
        if wave_list[0] > 30 and clap_list[9] > threshold:
            breaktime = True


    while breaktime == True:
        #start breaktime
        cp.pixels.fill(green)

        breaktime_scaled = 5 / 10 # 5 seconds divided by 10 neopixels

        # countdown
        for p in range(10):
            time.sleep(breaktime_scaled)
            cp.pixels[p] = (0, 0, 0)

        breaktime = False




