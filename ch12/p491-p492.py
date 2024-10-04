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


destinations = []
for destination in flights.values():
    destinations.append(destination.title())

print('destinations == ', destinations)

more_destinations = [destination.title() for destination in flights.values()]

print('more_destinations == ', more_destinations)


flight_times = []
for flight_time in flights.keys():
    flight_times.append(convert2ampm(flight_time))

print('flight_times == ', flight_times)

flight_times2 = [convert2ampm(flight_time) for flight_time in flights.keys()]

print('flight_times2 == ', flight_times2)

# flights2 = {}
#
# # Add your "for" loop here
# for time, destination in flights.items():
#     #print(convert2ampm(time), ' ', destination.title())
#     flights2[convert2ampm(time)] = destination.title()
#
# print()
# print("flights2:")
# pprint.pprint(flights2)
# print()
