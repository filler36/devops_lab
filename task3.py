left = int(input())
right = int(input())
ar = []

for a in range(left, right + 1):
    numbers = str(a)

    for i in numbers:
        if int(i) == 0 or a % int(i) != 0:
            break

    else:
        ar.append(a)

print(ar)
