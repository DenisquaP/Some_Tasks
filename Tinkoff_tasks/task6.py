n, m = map(int, input().split())
spirtits = {i: 1 for i in range(1, n + 1)}
gangs = [[i] for i in spirtits.keys()]
for i in range(m):
    question, *oth = map(int, input().split())
    if question == 1:
        if all([oth not in i for i in gangs]):
            for i in range(len(gangs)):
                if oth[0] in gangs[i]:
                    fir = i
                elif oth[1] in gangs[i]:
                    sec = i
            fir, sec = gangs[fir], gangs[sec]
            gangs.remove(fir)
            gangs.remove(sec)
            new_gang = [fir + sec]
            gangs += new_gang
            for i in new_gang[0]:
                spirtits[i] += 1

    elif question == 2:
        print("YES" if any([oth[0] in i and oth[1] in i for i in gangs]) else "NO") # noqa 501

    elif question == 3:
        print(spirtits[oth[0]])
