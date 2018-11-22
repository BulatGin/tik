from collections import OrderedDict

inp_data = {'a': 0.5, 'b': 0.25, 'c': 0.125, 'd': 0.125}

probs = OrderedDict(sorted(inp_data.items(), key=lambda i: i[0]))

# uncomment if you want to read alphabet and probabilities from stdin

# tmp = dict()
# n = int(input())
# for i in range(n):
#     x, p = input().split()
#     tmp[x] = float(p)
#
# probs = OrderedDict(sorted(tmp.items(), key=lambda i: i[0]))

initial_sections = {symb: [0, 0] for symb in probs}

buf = 0.0
for symbol, probability in probs.items():
    initial_sections[symbol][0] = buf
    buf += probability
    initial_sections[symbol][1] = buf

left = 0.0
right = 1.0

print('Введите строку для кодирования')
s = input()
for char in s:
    new_left = left + (right - left) * initial_sections[char][0]
    new_right = left + (right - left) * initial_sections[char][1]
    left = new_left
    right = new_right

print((right + left) / 2)
