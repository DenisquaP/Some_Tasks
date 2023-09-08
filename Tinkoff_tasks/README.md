# Задача 1
Однажды ковбой Джо решил обзавестись револьвером и пришёл в оружейный магазин. У ковбоя s долларов, а на выбор представлены n револьверов с ценами a1,a2,…,an​. 

Помогите ковбою Джо выбрать самый дорогой револьвер, который он может себе позволить или сообщите, что такого не существует. 

Формат входных данных

В первой строке даны целые числа n, s — количество револьверов в магазине и количество долларов у ковбоя Джо.

Во второй строке даны n целых чисел a1,a2,…,an — цены револьверов в магазине. 

Формат выходных данных

Выведите единственное целое число — цену самого дорого револьвера, который ковбой Джо сможет себе позволить, если такого револьвера нет, выведите 0.

___
# Задача 2
Однажды ковбой Джо нанялся в помощники шерифу. Шериф выдал ковбою Джо строку s и попросил собрать из её букв как можно больше слов sheriff. Каждая буква может использоваться не более чем в одном слове.

Ковбой Джо тут же приступил к заданию шерифа, но к сожалению, он не умеет читать. Помогите ковбою Джо. 

___
# Задача 3
Перед ковбоем Джо выложены n карт со значениями а1, a2, . . . , a7. Он хочет получить выигрышную последовательность карт со значениями b1, b2, ..., bn. Ковбой может выбрать непрерывный отрезок карт в своей последовательности [l, r] (1 <= l <= r <= n) и упорядочить карты в этом отрезке по неубыванию. Например, если перед ковбоем лежат карты {3, 3, 2, 5, 1, 5}, он может выбрать отрезок [2, 5] и получить последовательность {3, 1, 2, 3, 5, 5}. Получится ли у ковбоя Джо получить выигрышную последовательность с помощью применения вышеописанной операции ровно один раз? Формат входных данных В первой строке дано целое число п (1 < п < 2 • 105) -- количество карт в последовательности. Во второй строке даны п целых чисел а1, 02, . .., ар (1 < а; < 10°) - последовательность ковбоя Джо.
В третьей строке даны п целых чисел 61, 62, . ..., 6, (1 < 6; < 10°) - выигрышная последовательность.
Формат выходных данных:
Выведите «YES» (без кавычек), если Джо может получить выигрышную последовательность, иначе выведите «NO»

___
# Задача 4
На Диком западе ходят купюры номиналами a1, a2, a3, ..., am долларов. Однажды ковбой Джо решил ограбить банк. Он выбрал очень неудачный момент для ограбления, ведь сейчас в банке находятся ровно по две купюры каждого существующего номинала.
Ковбой Джо хочет украсть ровно п долларов, ни долларом больше, ни долларом меньше. Помогите ему или сообщите, что его план неосуществим.
Формат входных данных:
В первой строке даны целые числа п, т (1 <= n <= 10^9, 1 <= m <= 10) - необходимая ковбою Джо сумма и количество номиналов купюр. Во второй строке вводятся т попарно различных целых чисел 01, 02; . .. , Qm (1 < Q; < 10°) -
существующие номиналы купюр.
Формат выходных данных
Если ковбой Джо сможет украсть ровно п долларов, выведите число / - количество украденных купюр. Затем выведите к целых чисел - номиналы купюр. Если решений несколько, вы можете вывести любое.
В противном случае выведите - 1.

___
# Задача 6
Однажды ковбой Джо забрёл в жуткую заброшенную шахту, в которой обитают п духов с номерами 1, 2, . .. , n. Сейчас каждый дух состоит в банде из самого себя. В один момент времени каждый дух может находиться ровно в одной банде. По одиночке духи слабы, поэтому вскоре банды начнут объединяться. Когда две банды объединяются, создаётся новая банда, в которую попадают все духи из объединяющихся банд, в то время как старые банды распадаются. Ковбоя Джо оглушил душераздирающий крик, который сообщил ему о необходимости ответить на т
вопросов. Если ковбой Джо откажется отвечать на вопросы крика или ошибётся, то навечно сгинет в
заброшенной шахте.
Дух задаст m вопросов, каждый из которых относится к одному из трёх типов.
1. Духи x и у объединяются в банду. Если они уже находятся в одной банде, ничего не происходит
2. Крик спрашивает ковбоя Джо, находятся ли духи т и у в одной банде.
3. Крик спрашивает ковбоя Джо, в скольких бандах побывал дух х.

Например, если n = 7, а банды выглядели так: [1, 3], [4, 6, 2], [5], (7), и крик сообщил об объединении банд с духами 1 и 5, банды будут выглядеть так: [1, 5, 8], [4, 6, 2], [7]. 
Духи 1, 3, 5 побывали в двух бандах, духи 2, 4, 6, 7 в одной.
Формат входных данных
В первой строке даны целые числа n, m (1 < n, m < 2 • 10 ^5) - количество духов и вопросов крика.
Формат выходных данных:
Для каждого вопроса второго типа выведите <<YES»> или ««NO>> (без кавычек).