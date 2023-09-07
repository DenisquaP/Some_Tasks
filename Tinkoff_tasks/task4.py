need, n = map(int, input().split())
cash = list(map(int, input().split())) * 2

if sum(cash) < need:
    print(-1)
    exit()
elif sum(cash) == need:
    cash.sort()
    print(*cash)
    exit()
else:
    cash.sort()
    temp = cash[:]
    for _ in range(2):
        while temp:
            temp = temp[1:]
            if sum(temp) == need:
                print(len(temp))
                print(*temp)
                exit()
        temp = cash[::-1]
print(-1)
