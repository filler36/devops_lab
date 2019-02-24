from collections import Counter

n = int(input())
if n >= 1 and n <= 10**5:
    words = [input().strip() for _ in range(n)]
    counts = Counter(words)
    print(len(counts))
    print(*counts.values())
else:
    print("The n is not in allowed scope!")
