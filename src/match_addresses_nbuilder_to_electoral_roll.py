#! /usr/bin/env python3

import csv
import sys

electoral_role_filename = sys.argv[1]
nbuilder_filename = sys.argv[2]

PERSON_ID = 0
LOCAL_COUNCIL_COL = 13
ADDR_CITY_COL = 28
ADDR_POSTCODE_COL = 29

NB_POSTCODE_COL = 131
NB_PRIMARY_ADDR1 = 132
NB_PRIMARY_ADDR2 = 133
NB_EXTERNAL_ID = 6

people = dict()

with open(nbuilder_filename,'r') as nb_f:

    

    nb_csv = csv.reader(nb_f)
    nb_header = next(nb_csv)    

    
    for row in nb_csv:
        if row[NB_EXTERNAL_ID] == "":
            continue
        if row[NB_EXTERNAL_ID] in people:
            print(row)
            print( people[row[NB_EXTERNAL_ID]])
            print( "Duplicate External IDS")
            sys.exit()
        people[row[NB_EXTERNAL_ID]] = row
    

with open(electoral_role_filename, 'r') as elect_f:
    elect_csv = csv.reader(elect_f, delimiter='~')
    for row in elect_csv:
        pid = row[PERSON_ID]
        if pid in people:
            print(row)


