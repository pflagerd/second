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

just_freeport = {}
for time, destination in flights.items():
    if destination == "FREEPORT":
        just_freeport[convert2ampm(time)] = destination.title()

print("just_freeport:")
pprint.pprint(just_freeport)
print()

must_freeport2 = {convert2ampm(time): destination.title()
                  for time, destination in flights.items()
                  if destination == 'FREEPORT'}

print()
print("must_freeport2:")
pprint.pprint(must_freeport2)
print()












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
