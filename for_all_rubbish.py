def is_defended(attackers, defenders):
    '''
    Given two Arrays in which values are the power of each soldier, return true if you survive the attack or false if
    you perish.

    CONDITIONS

    Each soldier attacks the opposing soldier in the same index of the array. The survivor is the
    number with the highest value.
    If the value is the same they both perish
    If one of the values is empty(different array lengths) the non-empty value soldier survives.
    To survive the defending side must have more survivors than the attacking side.
    In case there are the same number of survivors in both sides, the winner is the team with the
    highest initial attack power. If the total attack power of both sides is the same return true.
    The initial attack power is the sum of all the values in each array.
    '''

    sum_d, sum_a = sum(defenders), sum(attackers)
    for a, d in [(a, d) for a, d in zip(attackers, defenders)]:
        if a > d:
            del defenders[defenders.index(d)]
        else:
            del attackers[attackers.index(a)]
    if len(attackers) == len(defenders):
        return sum_d >= sum_a
    return len(defenders) > len(attackers)


def how_much_o(string):
    '''
    :param string: Получает строку, состоящую из букв, задача в том, чтобы найти максимально длинную полседовательность
    букв О(Русских)
    :return: Возвращает длину большей последовательности
    '''
    return max(map(len, string.split('О')))


def finding(some_str, n=0):
    '''

    :param some_str: Строка, в которой может быть имя антон. Проверяет наличие букв из имени в строке и правильность
    последовательности букв
    :param n: количество проверенных букв
    :return: при правильной работе функции должна возвращать 5, ибо тру при сложении принимает значение 1
    '''
    ant = ['a', 'n', 't', 'o', 'n']
    if n == 4:
        return [True] if some_str.find(ant[4]) else [False]
    if ant[n] in some_str:
        return [True] + finding(some_str[some_str.index(ant[n+1]):], n + 1)
    return False


def task_21(num):
    '''
    21 задача из проекта Эйлера
    :param num: число
    :return: является ли число 'дружественным'
    '''
    a, b = [], []
    for i in range(1, num // 2 + 1):
        if num % i == 0: a.append(i)
    for i in range(1, sum(a) // 2 + 1):
        if sum(a) % i == 0: b.append(i)
    return num == sum(b)


def bouncing_balls(h, bounce, window):
    '''
    https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
    :param h: высота мальчика
    :param bounce: высота отскока
    :param window: высота окна мамы
    :return:
    '''
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    now_h, count = h * bounce, 1
    while now_h > window:
        count += 2
        now_h *= bounce
    return count
