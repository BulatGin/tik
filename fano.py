from collections import OrderedDict


def fano_code(probs_: OrderedDict):
    if len(probs_) == 1:
        return
    if len(probs_) == 2:
        probs_as_list = list(probs_.items())
        codes[probs_as_list[0][0]] += '0'
        codes[probs_as_list[1][0]] += '1'
        return

    left_sub_probs = OrderedDict()
    right_sub_probs = probs_.copy()
    left_sum = 0.0
    right_sum = sum(probs_.values())
    diff = right_sum - left_sum
    for symb, prob in probs_.items():
        left_sum += prob
        right_sum -= prob
        if abs(right_sum - left_sum) > diff:
            break
        diff = abs(right_sum - left_sum)
        left_sub_probs[symb] = prob
        del right_sub_probs[symb]
    for symb in left_sub_probs.keys():
        codes[symb] += '0'
    for symb in right_sub_probs.keys():
        codes[symb] += '1'

    fano_code(left_sub_probs)
    fano_code(right_sub_probs)


inp_data = {'a': 0.5, 'b': 0.25, 'c': 0.125, 'd': 0.125}

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

codes = {symb: '' for symb in probs.keys()}

fano_code(probs)

for symb, code in sorted(codes.items()):
    print(symb, code, end='\n')
