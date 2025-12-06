from aocd import get_data, submit

data = get_data(year=2025, day=2)
exm = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""

strings = data.replace("\n", "").split(",")
res = 0

for s in strings:
    a, b = s.split("-")
    for i in range(2, 11):
        if len(a) % i == 0:
            if int(a[:len(a) // i] * i) < int(a):
                first = int(a[:len(a) // i]) + 1
            else:
                first = int(a[:len(a) // i])
        else:
            first = int("1" + ("0" * (len(a) // i)))
        if len(b) % i == 0:
            if int(b[:len(b) // i] * i) <= int(b):
                last = int(b[:len(b) // i])
            else:
                last = int(b[:len(b) // i]) - 1
        else:
            last = 0 if len(b) // i == 0 else int("9" * (len(b) // i))
        print(i, first, last)
        for j in range(first, last + 1):
            flag = True
            for k in range(1, len(str(j))):
                if len(str(j)) % k == 0:
                    flag2 = True
                    val = str(j)[:k]
                    for l in range(len(str(j)) // k):
                        if str(j)[l * k:(l + 1) * k] != val:
                            flag2 = False
                    if flag2:
                        flag = False
            if flag:
                print(str(j) * i)
                res += int(str(j) * i)

print(res)
submit(res, year=2025, day=2, part='b')
