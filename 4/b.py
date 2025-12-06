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

resi = 0
res = 0
mp = [list(x) for x in data.split('\n') if x]
while res > 0 or resi == 0:
    res = 0
    l = []
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
                l.append((int(cur.real), int(cur.imag)))
    for pos in l:
        mp[pos[0]][pos[1]] = 'x'
    for i in range(len(mp)):
        pass
        # print(''.join(mp[i]))
    for pos in l:
        mp[pos[0]][pos[1]] = '.'
    resi += res
    print(len(l))

print(resi)
# submit(resi, year=2025, day=4, part='b')
