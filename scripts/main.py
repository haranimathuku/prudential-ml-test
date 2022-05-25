#!/usr/bin/python3

import logging
import sys, getopt
from funs import calc_bmi, calc_quote

logging.basicConfig(
        format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO)

LOGGER = logging.getLogger(__file__)

def main(argv):
    usage = 'Enter the command in this format  "main.py -predict <age> <gender> <height> <weight> <discount>"'
	
   # checking whether the given input format is correct or not
    if (len(argv) == 6) and argv[0] == '-predict':
        age = int(argv[1])
        gender = argv[2]
        height = int(argv[3])
        weight = int(argv[4])
        discount = int(argv[5])
    else:
        print(usage)
        sys.exit(2)

    LOGGER.info("Quote calculation started")
    bmi = calc_bmi(height, weight)
    quote = calc_quote(age, gender, bmi, discount)
    print("Your quote is", quote)
    LOGGER.info("Completed")

if __name__ == "__main__":
    # Run the prediction
    main(sys.argv[1:])