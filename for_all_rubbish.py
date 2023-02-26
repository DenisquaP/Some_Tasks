import itertools


def is_defended(attackers, defenders):
    '''Given two Arrays in which values are the power of each soldier, return
    true if you survive the attack or false if
    you perish.

    CONDITIONS

    Each soldier attacks the opposing soldier in the same index of the array.
    The survivor is the
    number with the highest value.
    If the value is the same they both perish
    If one of the values is empty(different array lengths) the non-empty
    value soldier survives.
    To survive the defending side must have more survivors than the
    attacking side.
    In case there are the same number of survivors in both sides, the winner
    is the team with the
    highest initial attack power. If the total attack power of both sides is
    the same return true.
    The initial attack power is the sum of all the values in each array.'''

    chained = itertools.zip_longest(attackers, defenders, fillvalue=0)
    win = [a < d for a, d in chained]
    if win.count(True) > len(win) / 2:
        return True
    else:
        # con - условие
        con = win.count(True) == len(win) / 2
        con_2 = sum(attackers) < sum(defenders)
        return True if con and con_2 else False


def how_much_o(string):
    """
    :param string: Получает строку, состоящую из букв, задача в том, чтобы
    найти максимально длинную последовательность
    букв О(Русских)
    :return: Возвращает длину большей последовательности
    """
    return max(map(len, string.split('О')))


def finding(some_str, n=0):
    """
    :param some_str: Строка, в которой может быть имя Антон. Проверяет наличие
    букв из имени в строке и правильность
    последовательности букв
    :param n: количество проверенных букв
    :return: при правильной работе функции должна возвращать 5, ибо тру при
    сложении принимает значение 1
    """
    ant = ['a', 'n', 't', 'o', 'n']
    if n == 4:
        return [True] if some_str.find(ant[4]) else [False]
    if ant[n] in some_str:
        return [True] + finding(some_str[some_str.index(ant[n+1]):], n + 1)
    return False


def task_21(num):
    """
    21 задача из проекта Эйлера
    :param num: число
    :return: является ли число 'дружественным'
    """
    a, b = [], []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            a.append(i)
    for i in range(1, sum(a) // 2 + 1):
        if sum(a) % i == 0:
            b.append(i)
    return num == sum(b)


def bouncing_balls(h, bounce, window):
    """
    https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
    :param h: высота окна мальчика
    :param bounce: высота отскока (в %) 0 < bounce < 1
    :param window: высота окна мамы
    :return:
    """
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    now_h, count = h * bounce, 1
    while now_h > window:
        count += 2
        now_h *= bounce
    return count


def bingo(ticket, win):
    '''
    https://www.codewars.com/kata/57f625992f4d53c24200070e/python
    ticket - номер билета в формате ['ABC', 65]
    win - минимальное число выигрышей (строка в списке содержит символ ascii)
    Сделал 2 решения: простое и короткое)
    '''
    count = [i[0].count(chr(i[1])) for i in ticket]
    # count = 0
    # for i in ticket:
    #     count += i[0].count(chr(i[1]))
    #     if any([j == chr(i[1]) for j in i[0]]):
    #         count += 1
    # return 'Winner!' if count >= win else 'Loser!'
    return 'Winner!' if sum(count) >= win else 'Loser!'


def spok(first_player, second_player):
    '''
    Камень, ножницы, бумага, ящерица, спок - игра из
    сериала "Теория большого взрыва"
    '''
    game_tuples = {
        ('ножницы', 'бумага'),
        ('бумага', 'камень'),
        ('камень', 'ящерица'),
        ('ящерица', 'Спок'),
        ('Спок', 'ножницы'),
        ('ножницы', 'ящерица'),
        ('ящерица', 'бумага'),
        ('Спок', 'камень'),
        ('камень', 'ножницы')
    }
    if first_player == second_player:
        return 'Draw'
    else:
        if (first_player, second_player) in game_tuples:
            return 'First'
        else:
            return 'Second'


def snail(snail_map):
    '''
    https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
    Задача по выводу списка nxn по спирали
    Можно решить с помощью нампай, но и без него нормально)
    '''
    expected = []
    while len(snail_map) > 1:
        expected.extend(snail_map[0])
        del snail_map[0]
        snail_map = list(zip(*snail_map))[::-1]  # Поворот на 90
    expected.extend(snail_map[0])  # Добавление последнего элемента
    return expected


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
# print(snail(array))


def generate_hashtag(s):
    '''https://www.codewars.com/kata/52449b062fb80683ec000024/python'''
    if len(s) > 140 or not bool(s):
        return False
    return '#' + ''.join(map(lambda i: i.capitalize(), s.split()))


def narcissistic(value):
    length = len(str(value))
    res = [int(i)**length for i in str(value)]
    return sum(res) == value


print(narcissistic(7))
