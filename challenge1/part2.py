#Name: Justin Sadler
#Date: 2022-12-06
# Script to solve the part 2first challenge

import os
import heapq

directory = os.path.realpath(os.path.dirname(__file__))
heap = [] # heap containing the 3 bigest calorie counts

with open(directory + "/input.txt", "r") as f:

    calories = 0 # The number of calories the current elf is carrying
    while True:

        line = f.readline()
        if not line: break

        # If line is all whitespac
        if line.isspace():
            # Insert calorie count into min heap
            heapq.heappush(heap, calories)
            # if the heap is bigger than 3, remove 1 smallest item from
            # heap. 
            if len(heap) > 3:
                heapq.heappop(heap)
            calories = 0
        else:
            calories += int(line)


with open(directory + "/part2output.txt", "w") as f:
    f.write(str(sum(heap)))

with open(directory + "/part2output.txt", "r") as f:
    print(f.read())