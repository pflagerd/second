
data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)

print(data)
print(evens)


data= [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)

print(data)
print(words)


data = list('So long and thanks for all the fish'.splot())
title = []
for word in data:
    title.append(word.title())

print(data)
print(words)

