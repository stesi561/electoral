#! /usr/bin/env python3

import csv
import sys

filenames = sys.argv[1:]

NB_EXTERNAL_ID = 0

nb_ids = dict()
blanks = 0
dups = 0

rows = dict()

matches = dict()

for filename in filenames:
    if "-608-2016-" in  filename:
        continue
    with open(filename,'r') as nb_f:
        print("reading: {}".format(filename))
    

        nb_csv = csv.reader(nb_f)   
        next(nb_csv)
    
        for row in nb_csv:
            if row[NB_EXTERNAL_ID] == "":
                blanks+= 1
            
            elif row[NB_EXTERNAL_ID] in nb_ids:
                print(row)
                print(rows[row[NB_EXTERNAL_ID]])
                
                dups+=1
                m = (filename, nb_ids[row[NB_EXTERNAL_ID]]) 
                if m not in matches:
                    matches[m] = 0
                matches[m]+= 1
                
            else:
                nb_ids[row[NB_EXTERNAL_ID]] = filename
                rows[row[NB_EXTERNAL_ID]] = row[0:4]
    



print("Unique: {}".format(len(nb_ids)))
print("Dups: {}".format(dups))
print("Blanks: {}".format(blanks))
for m in matches:
    print("{}:\t{}".format(m[0:4], matches[m]))
