#Name: Justin Sadler
#Date: 2022-12-06
# Script to solve the first challenge
import os

directory = os.path.realpath(os.path.dirname(__file__))
max_calories = 0 # The max amoutn of calories an individual elf is carrying

with open(directory + "/input.txt", "r") as f:

    calories = 0 # The number of calories the current elf is carrying
    while True:

        line = f.readline()
        if not line: break

        # If line is all whitespac
        if line.isspace():
            max_calories = max(max_calories, calories)
            calories = 0
        else:
            calories += int(line)


with open(directory + "/out.txt", "w") as f:
    f.write(str(max_calories))