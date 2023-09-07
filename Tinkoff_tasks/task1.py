n, s = map(int, input().split())
costs = list(map(int, input().split()))
costs.sort()

for i in costs[::-1]:
    if s >= i:
        print(i)
        exit()

print(0)
