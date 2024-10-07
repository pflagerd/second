from datetime import datetime
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[convert2ampm(k)] = v.title()

print("flights:")
pprint.pprint(flights)
print()

destinations = set(flights.values())
print(destinations)


westEnd = []
for k, v in flights.items():
    if v == 'West End':
        westEnd.append(k)
print(westEnd)

print([k for k, v in flights.items() if v == 'West End'])


for destination in set(flights.values()):
    print(destination, '->', [k for k, v in flights.items() if v == destination])


when = {}
for destination in set(flights.values()):
    when[destination] = [k for k, v in flights.items() if v == destination]

pprint.pprint(when)


when = {}
for destination in set(flights.values()):
    when[destination] = [k for k, v in flights.items() if v == destination]

pprint.pprint(when)

pprint.pprint({destination: [k for k, v in flights.items() if v == destination] for destination in set(flights.values())})


