import csv

with open('buzzers.csv') as data:
    for line in csv.reader(data):
        #print(type(line))
        print(line)
