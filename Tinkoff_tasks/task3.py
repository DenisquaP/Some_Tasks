from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a == b:
    print("YES")
    exit()
elif Counter(a) == Counter(b):
    start = 0
    fin = 0
    for i in range(n):
        if a[i] != b[i]:
            if start:
                fin = i
            else:
                start = i
    a = a[:start] + sorted(a[start:fin + 1]) + a[fin + 1:]
    print("YES" if a == b else "NO")
else:
    print("NO")
