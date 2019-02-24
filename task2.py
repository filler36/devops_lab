import random

n = int(input())
ar = []

for i in range(n):
    ar.append(random.randint(1, 100))

num = ar[0]
max_frq = 1
for i in range(n - 1):
    frq = 1
    for k in range(i + 1, n):
        if ar[i] == ar[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = ar[i]

print(ar)
if max_frq > 1:
    print('Number', num, 'occurs', max_frq, 'times in list')
else:
    print('There is no elements that occurs more than 1 times')
