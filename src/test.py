# Spinners
# A collection of spinners for use in the terminal.
# Github: https://www.github.com/0x4248/Spinners
# By: 0x4248

import sys
import time

spinners = open("src/spinners.txt", "r").read().split("\n")

line = input("What spinner would you like to test? ")
line = int(line)
line = line - 1
speed = input("Seconds between frames? ")
speed = float(speed)

spinner = spinners[line]
while True:
    for frame in spinner:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(speed)