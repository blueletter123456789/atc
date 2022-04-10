import itertools

s, k = input().split()
s, k = list(s), int(k)
words = set(itertools.permutations(s))
words = sorted(words)
print(''.join(words[k-1]))
