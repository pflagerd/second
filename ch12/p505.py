from datetime import datetime
import pprint

vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel."
found = set()
for v in vowels:
    if v in message:
        found.add(v)

print(found)