from aocd import get_data, submit

data = get_data(year=2025, day=5)
exm = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

ranges, ids = [list(filter(None, x.split('\n'))) for x in data.split('\n\n')]
res = 0
l = []


def ins(a, b):
    for iv in l:
        if iv[0] <= a <= iv[1]:
            l.remove(iv)
            ins(iv[0], max(b, iv[1]))
            return
        elif iv[0] <= b <= iv[1]:
            l.remove(iv)
            ins(min(a, iv[0]), iv[1])
            return
        elif a <= iv[0] <= iv[1] <= b:
            l.remove(iv)
    l.append((a, b))


for s2 in ranges:
    a, b = map(int, s2.split('-'))
    ins(a, b)

print(sorted(l))

for iv in l:
    res += iv[1] - iv[0] + 1

print(res)
submit(res, year=2025, day=5, part='b')
