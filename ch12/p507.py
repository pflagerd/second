from datetime import datetime
import pprint

names = ()

try:
    for n in ('John', 'Paul', 'George', 'Ringo'):
        names.append(n)
except AttributeError:
    pass

for i in [x * 3 for x in [1, 2, 3, 4, 5]]:
    print(i)

for i in (x * 3 for x in [1, 2, 3, 4, 5]):
    print(i)
