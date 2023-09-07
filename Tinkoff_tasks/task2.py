s = input()
letters = {key: 0 for key in 'sherif'}

for i in s:
    if letters.get(i) or i in 'sheriff':
        letters[i] += 1
letters['f'] = letters['f'] // 2

maybe_result = min(letters.values())
if all([i >= maybe_result for i in letters.values()]):
    print(maybe_result)
else:
    print(0)
