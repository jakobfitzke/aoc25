from aocd import get_data, submit
from functools import reduce

data = get_data(year=2025, day=6)
exm = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

strings = list(filter(None, data.split('\n')))
res = 0
a = strings.pop()
op = list(filter(None, a.split(' ')))
le = []
for i in range(len(a)):
    if a[i] == '+' or a[i] == '*':
        le.append(0)
    else:
        le[-1] += 1
le[-1] += 1

numbers = [['' for y in range(x)] for x in le]
print(numbers)
print(le)

for s in strings:
    i = 0
    ix = 0
    while ix < len(le):
        for j in range(le[ix]):
            if s[i] != ' ':
                numbers[ix][j] += s[i]
            i += 1
        ix += 1
        i += 1
print(numbers)
acc = []
for i in range(len(numbers)):
    print(list(filter(None, numbers[i])))
    if op[i] == '+':
        acc.append(sum(map(int, filter(None, numbers[i]))))
    else:
        prod = 1
        for num in filter(None, numbers[i]):
            prod *= int(num)
        acc.append(prod)

print(acc)
res = sum(acc)
print(res)
submit(res, year=2025, day=6, part='b')
