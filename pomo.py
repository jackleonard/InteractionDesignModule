#import time

#initial = time.monotonic() #after reading up it says circuit python can only use this. Has to be in seconds

#print("Pomodoro timer begins!")

#for i in range (4):
 #   t = 25*60       # 25 minute break
  #  while t:
   #     mins = t // 60 
    #   secs = t % 60
     #   timer = '{:02d}:{:02d}'.format(mins, secs)
      #  print(" " + timer, end="\r") 
       # time.sleep(1)
        #t -= 1

#print("Take a break!")

#t = 5*60        # 5 minute break
#while t:
 #   secs = t % 60
 #   mins = t // 60
 #   timer = '{:02d}:{:02d}'.format(mins, secs)
 #   print(timer, end="\r") 
 #   time.sleep(1)
#    t -= 1
#print("Back to Work!")



import time
from adafruit_circuitplayground.express import cp
from random import random
from math import cos
import neopixel 




cp.pixels.brightness = 0.05
pixel_off_state = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

MINUTE = 60
WORK_LENGTH = 25 * MINUTE
BREAK_LENGTH = 5 * MINUTE


#PEAK_COLOR = (100, 0, 255)
#NUM_PIXELS = 10


start = time.monotonic()

def start_timer():
    for l in range(NUM_PIXELS):
        pixels[l] = PEAK_COLOR
    pixels.show()
    time.sleep(1)

def pomo_begin():
    print("Pomodoro begin")
    for i in range(9, -1, -1): #range(start, stop, step):
        pixels[i] = (255, 0, 0)
        pixels.show()
        time.sleep(1)

    pixels.fill((255, 255, 0))
    pixels.show()

    for i in range(NUM_PIXELS):
        pixels[i] = (255, 0, 0)
        pixels.show()
        time.sleep(1)

pixels = neopixel.NeoPixel(board.NEOPIXEL, NUM_PIXELS, brightness=0.1, auto_write=False)
pixels.fill(0)
pixels.show()