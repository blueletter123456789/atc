name_set = set(['ABC', 'ARC', 'AGC', 'AHC'])
for _ in range(3):
    s = input()
    name_set.remove(s)
print(name_set.pop())
