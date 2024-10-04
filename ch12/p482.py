import csv
import pprint

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

    print(type(flights))
    print(flights)

    pprint.pprint(flights)