#Name: Justin Sadler
#Date: 2022-12-06
# Script to solve first challenge of day 6 

import os
import sys

directory = os.path.realpath(os.path.dirname(__file__))

def solve(datastream):

    # i starts on 4th char
    for i in range(14 - 1,len(datastream)):
        last14 = datastream[i - 14 + 1: i + 1]
        if len(set(last14)) == 14:
            break
    return i + 1

if len(sys.argv) > 1:
    print(solve(sys.argv[1]))
else:
    with open(directory + "/input.txt", "r") as infile:
        with open(directory + "/out1.txt", "w") as outfile:
            res = solve(infile.read())
            print(res)
            outfile.write(str(res))