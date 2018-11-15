
import argparse
from random import randint

# Define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('count', type = int, help = 'Count of random integers to be generated')

# Add optional arguments
parser.add_argument('-r', '--range', metavar = ('lower', 'upper'), nargs = 2, type = int, default = [0, 10], help = 'Integer range [a, b] from which the random numbers will be chosen')

parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Verbose mode')

# Parse command-line arguments
args = parser.parse_args()

# Program
if args.verbose:
    print("Generating {:d} random integer in the range [{:d}, {:d}]".format(args.count, args.range[0], args.range[1]))
            
for i in range(args.count):
    print(randint(args.range[0], args.range[1]))