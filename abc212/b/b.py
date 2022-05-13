from collections import defaultdict

passwd = input()
num_dict = defaultdict(int)
cnt = 0

for i in range(len(passwd)-1):
    if (int(passwd[i+1]) - int(passwd[i])) % 10 == 1:
        cnt += 1
    num_dict[passwd[i]] += 1

num_dict[passwd[i+1]] += 1

if cnt != 3 and num_dict[passwd[i+1]] != 4:
    print('Strong')
else:
    print('Weak')
