
import argparse
from random import randint

# Define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('count', type = int, help = 'Count of random integers to be generated')

# Parse command-line arguments
args = parser.parse_args()

# Program
for i in range(args.count):
    print(randint(0, 10))