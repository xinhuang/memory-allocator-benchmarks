#!/bin/python
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

import subprocess

# Parameters: <threads> <inner-loop> <object-size> <iterations>
cmd = ['./cache-scratch', 'P', '100', '8', '1000000']
subprocess.call(cmd)
# subprocess.Popen("cache-thrash P 100 8 1000000")

# <seconds> <min-obj-size> <max-obj-size> <objects> <iterations> <rng seed> <num-threads>
# ./larson 10 7 8 1000 10000 1 P

# Parameters: <number-of-threads> <iterations> <num-objects> <work-interval> <object-size>
# ./threadtest P 1000 10000 0 8

# ./t-test1
