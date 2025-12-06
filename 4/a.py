from aocd import get_data, submit

data = get_data(year=2025, day=4)
exm = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

mp = list(filter(None, data.split('\n')))
res = 0
for i in range(len(mp)):
    for k in range(len(mp[0])):
        cur = i + k * 1j
        ct = 0
        for off in (-1 - 1j, -1, -1 + 1j, -1j, +1j, 1 - 1j, 1, 1 + 1j):
            curn = cur + off
            if 0 <= curn.real < len(mp) and 0 <= curn.imag < len(mp[0]):
                ct += mp[int(curn.real)][int(curn.imag)] == '@'
        if mp[int(cur.real)][int(cur.imag)] == '@' and ct < 4:
            res += 1

print(res)
submit(res, year=2025, day=4, part='a')
