from aocd import get_data, submit
from shapely.geometry import Point, Polygon, box

data = get_data(year=2025, day=9)
exm = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

strings = list(filter(None, data.split('\n')))
res = 0
points = []
for s in strings:
    points.append(tuple(map(int, s.split(','))))

poly = Polygon(points)

m = 0
for i in range(len(points)):
    if i % 20 == 0:
        print(i)
    for j in range(i, len(points)):
        rect = box(points[i][0], points[i][1], points[j][0], points[j][1])
        if poly.covers(rect):
            area = (abs(points[j][0] - points[i][0]) + 1) * (abs(points[j][1] - points[i][1]) + 1)
            if area > m:
                m = area

res = m
print(res)
# submit(res, year=2025, day=9, part='b')
