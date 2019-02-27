def calc(x, y, z, n):
    ar = []
    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                if i + j + k != n:
                    print([i, j, k])
                    ar.append([i, j, k])
    return ar


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    calc(x, y, z, n)
