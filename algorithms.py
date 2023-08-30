from collections import deque


def recur(num):
    # Сумма чисел из которого состоит num
    if num < 10:
        return num
    else:
        return num % 10 + recur(num//10)


def recur_2(lis):
    # Длина списка по рекурсии
    if lis == []:
        return 0
    return 1 + recur_2(lis[1:])


def quick_sort(lis):
    if len(lis) < 2:
        return lis

    # Выбираем опорный элемент
    pivot = lis[0]
    less = [i for i in lis if i < pivot]
    grather = [i for i in lis if i > pivot]

    # Рекурсия пока всё не отсортируется
    return quick_sort(less) + [pivot] + quick_sort(grather)


# Поиск в ширину
def bredth_first_search(pers):
    # Двусторонняя очередь
    search_queue = deque()
    search_queue += pers['you']
    searched = []
    while search_queue:
        check = search_queue.popleft()
        if check not in searched:
            if dead_check(check):
                return check + ' is dead'
            # Добавление следующего узла
            if pers.get(check):
                search_queue += pers[check]
            searched += [check]
    return 'Dead character isn`t found'


def dead_check(character):
    return character == 'Horatio'


persons = {
    'you': ['Artyom', 'Marcus', 'Lara'],
    'Artyom': ['Miller', 'Ulman'],
    'Marcus': ['Sitara', 'Wrench', 'Josh', 'Horatio'],
    'Lara': ['Jonah']
}


# Алгоритм Дейкстры
def dijkstra(graph, costs, parents):
    processed = []
    node = min_cost(processed, costs)
    while node is not None:
        cost = costs[node]
        neibors = graph[node]
        for n in neibors.keys():
            new_cost = cost + neibors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = min_cost(processed, costs)

    return parents, costs['fin']


def min_cost(processed, costs):
    # 0 имя узла,  1 цена узла
    min = [None, float('inf')]
    for key, val in costs.items():
        if val < min[1] and key not in processed:
            min[0] = key
            min[1] = val
    return min[0]


graph = {
    'start': {
        'a': 2, 'b': 1
    },
    'a': {'d': 5},
    'b': {'c': 4},
    'c': {'e': 7},
    'd': {'c': 1, 'fin': 3},
    'e': {'fin': 2},
    'fin': {}
}

costs = {
    'a': 2,
    'b': 1,
    'c': float('inf'),
    'd': float('inf'),
    'e': float('inf'),
    'fin': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'c': None,
    'd': None,
    'e': None,
    'fin': None
}


# Жадный алгоритм. Покрытие штатов радиостанциями
stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}

states_needed = {
    'mt', 'wa', 'or', 'id', 'nv',
    'ut', 'ca', 'az'
}


# Выбирает станции, которые покрывают наибольшее количество непокрытых штатов
def some_hungry_alg(radio, needed):
    stations_selected = set()
    while needed:
        best_station = None
        states_covered = set()
        for station, states in radio.items():
            covered = needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        stations_selected.add(best_station)
        needed -= states_covered
    return stations_selected
