#! /usr/bin/env python3

import csv
import sys

nbuilder_filename = sys.argv[1]


with open(nbuilder_filename,'r') as nb_f:

    nb_csv = csv.reader(nb_f)

    header = next(nb_csv)
    for col_id, col in zip(range(len(header)),header):
        print("{}\t{}".format(col_id,col))
