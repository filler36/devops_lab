key = input([])
keystring = 'qwertyuiopasdfghjklzxcvbnm'
ar = list(keystring)

for i in (i for i, x in enumerate(ar) if x == key):
    if key == 'm':
        print(ar[0])
    else:
        print(ar[i + 1])
