d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for k in d:
    print(k, d.get(k), end=' ', sep='')
print()

d['a'] += 1
print(d)
d['a'] -= 1

print(d.keys())
