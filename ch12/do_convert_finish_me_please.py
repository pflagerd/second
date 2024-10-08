from datetime import datetime
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

print("flights:")
pprint.pprint(flights)
print()

flights2 = {}

# Add your "for" loop here

print()
print("flights2:")
pprint.pprint(flights2)
print()
