def appender(n):
    ''' Чтобы не повторять код вынес в функцию. Она считывает файл. '''
    list = []
    for _ in range(n):
        list.append(i.readline().rstrip('\n'))
    return list


def seats(pas):
    splited = pas.split(' ')
    # количество пассажиров
    num = int(splited[0])
    # Для поиска требуемого сидения
    position = positions.get(' '.join([splited[1], splited[2]]))
    # сторона в самолете
    side = sides.get(splited[1])
    # проверяю есть ли места
    if any(['.'*num in i.split('_')[side] for i in lines]):
        for i in lines:
            if i[position] == '.' and ('.'*num in i.split('_')[side]):
                if position in [0, 4]:
                    # возвращаю место от которого начинать отсчет в цикле
                    return position, lines.index(i), num
                else:
                    # то же самое, что и выше, но теперь возвращаю место крайнего левого пассажира, а не главного # noqa 501
                    return position - num + 1, lines.index(i), num
    else:
        return False


# Словари для поиска свободных мест
positions = {
    'left window': 0,
    'left aisle': 2,
    'right window': 6,
    'right aisle': 4
}

sides = {
    'left': 0,
    'right': 1
}

plane = {
    0: 'A',
    1: 'B',
    2: 'C',
    4: 'D',
    5: 'E',
    6: 'F'
}

with open('input.txt', 'r') as i:
    n = int(i.readline().rstrip('\n'))
    lines = appender(n)

    m = int(i.readline().rstrip('\n'))
    passangers = appender(m)


with open('output.txt', 'w') as o:
    for pas in passangers:
        a = seats(pas)
        if a:
            # str(a[1]+1) это ряд, он статичен
            # plane[i] это место человека
            s = [str(a[1]+1)+plane[i] for i in range(a[0], a[0]+a[2])]
            # Обновление ряда самолета для отображения мест в файле
            lines[a[1]] = lines[a[1]][:a[0]] + 'X'*a[2] + lines[a[1]][a[0]+a[2]:]  # noqa 501
            o.write(f'Passengers can take seats: {s}\n')
            [o.write(line+'\n') for line in lines]
            # Обновление ряда самолета
            lines[a[1]] = lines[a[1]][:a[0]] + '#'*a[2] + lines[a[1]][a[0]+a[2]:]  # noqa 501
        else:
            o.write('Cannot fulfill passengers requirements\n')
