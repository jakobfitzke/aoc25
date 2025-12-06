from aocd import get_data, submit

data = get_data(year=2025, day=3)
exm = """987654321111111
811111111111119
234234234234278
818181911112111
"""

strings = filter(None, data.split('\n'))
res = 0
for s in strings:
    out = ""
    a = -1
    for i in range(12):
        a = max(list(range(a + 1, len(s) - 11 + i)), key=lambda x: int(s[x]))
        out += s[a]
    print(out)
    res += int(out)

print(res)
submit(res, year=2025, day=3, part='b')
