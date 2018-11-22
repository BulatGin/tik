import math
from collections import OrderedDict


def float2bin(number, places=10):
    res = ''

    fractional = number
    for x in range(places):
        integer, fractional = str(fractional * 2).split(".")
        fractional = float('0.' + fractional)
        res += integer

    return res


inp_data = {'a': 0.10, 'b': 0.20, 'c': 0.10, 'd': 0.10, 'e': 0.35, 'f': 0.15}

probs = OrderedDict(sorted(inp_data.items(), key=lambda i: i[1], reverse=True))

# uncomment if you want to read alphabet and probabilities from stdin
#
# tmp = dict()
# n = int(input())
# for i in range(n):
#     x, p = input().split()
#     tmp[x] = float(p)
#
# probs = OrderedDict(sorted(tmp.items(), key=lambda i: i[1], reverse=True))

cum_sums = dict()
cumulative_sum = 0.0

for symb, prob in probs.items():
    cum_sums[symb] = cumulative_sum
    cumulative_sum += prob

codes = dict()

for symb, cum_sum in cum_sums.items():
    codes[symb] = float2bin(cum_sum, math.ceil(-math.log2(probs[symb])))

for symb, code in sorted(codes.items()):
    print(symb, code, end='\n')
