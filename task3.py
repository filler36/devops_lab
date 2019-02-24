left = int(input())
right = int(input())
ar = []

for a in range(left, right + 1):
    numbers = str(a)
    flag = 0

    for i in numbers:
        if int(i) == 0 or a % int(i) != 0:
            flag = 1
            break

    if flag == 0:
        ar.append(a)

print(ar)
