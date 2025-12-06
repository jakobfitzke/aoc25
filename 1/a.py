from aocd import get_data, submit

data = get_data(year=2025, day=1)
exm = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

strings = filter(None, data.split('\n'))
res = 0
x = 50
for s in strings:
    d = s[0]
    n = int(s[1:])
    if d == "R":
        x = (x + n) % 100
    if d == "L":
        x = (x - n + 100) % 100
    if x == 0:
        res += 1

print(res)
submit(res, year=2025, day=1, part='a')
