w = int(input())

print(297)
out_lst = list()
for i in range(1, 100):
    out_lst += [str(i), str(i*100), str(i*10000)]
print(' '.join(out_lst))
