import time
from RF24 import *

radio = RF24(22, 0)
pipes = [0xF0F0F0F0E1, 0xF0F0F0F0D2]  # Set the pipe addresses

radio.begin()
radio.setChannel(0x60)
radio.openWritingPipe(pipes[1])

message = "1"

while True:
    radio.write(message)
    print("Sent:", message)
    time.sleep(1)