from queue import PriorityQueue, Empty

ans = PriorityQueue()
codes = dict()

n = int(input())
for i in range(n):
    x, p = input().split()
    ans.put((float(p), [x]))
    codes[x] = ''

try:
    while True:
        first = ans.get_nowait()
        second = ans.get_nowait()
        for elem in first[1]:
            codes[elem] = '0' + codes[elem]
        for elem in second[1]:
            codes[elem] = '1' + codes[elem]
        sum = (first[0] + second[0], first[1] + second[1])
        ans.put(sum)
except Empty:
    for symb, code in sorted(codes.items()):
        print(symb, code, end='\n')
