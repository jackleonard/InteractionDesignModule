'''
Class written based on this example: https://learn.adafruit.com/make-it-sense/circuitpython-3
Class sound. Used to retrieve sound magnitude.
Code modified into a class by Laura Maye.
'''
import array
import math
import audiobusio
import board

class Sound:

    def __init__(self):
        self.__samples = array.array('H', [0] * 160)
        self.__mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,sample_rate=16000,bit_depth=16)

    def start(self):
        try:
            self.__mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,sample_rate=16000,bit_depth=16)
        except:
            print("mic already started")

    def stop(self):
        try:
            self.__mic.deinit()
        except:
            print("mic already stopped")

    def record(self):
        self.__mic.record(self.__samples, len(self.__samples))

    def sound_level(self):
        minbuf = int(self.mean())
        sum_of_samples = sum(
            float(sample - minbuf) * (sample - minbuf)
            for sample in self.__samples
        )
        return math.sqrt(sum_of_samples / len(self.__samples))

    def mean(self):
        return sum(self.__samples) / len(self.__samples)



