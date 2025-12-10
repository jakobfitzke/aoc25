from aocd import get_data, submit
from operator import mul
from functools import reduce

data = get_data(year=2025, day=8)
exm = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


class UnionFind:
    def __init__(self, size):
        # Initialize the parent array with each
        # element as its own representative
        self.parent = list(range(size))

    def find(self, i):
        # If i itself is root or representative
        if self.parent[i] == i:
            return i

        # Else recursively find the representative
        # of the parent
        return self.find(self.parent[i])

    def unite(self, i, j):
        # Representative of set containing i
        irep = self.find(i)

        # Representative of set containing j
        jrep = self.find(j)

        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep


strings = filter(None, data.split('\n'))
res = 0
poses = []
for s in strings:
    poses.append(list(map(int, s.split(','))))

connected = UnionFind(len(poses))
edges = []

for j in range(len(poses)):
    for k in range(j + 1, len(poses)):
        edges.append(((j, k), ((poses[j][0] - poses[k][0]) ** 2 + (poses[j][1] - poses[k][1]) ** 2 + (
                poses[j][2] - poses[k][2]) ** 2) ** .5))

connections = set()

edges.sort(key=lambda x: x[1])
eu = 0
for edge in edges:
    print(eu)
    print(poses[edge[0][0]], poses[edge[0][1]])
    if eu == len(poses) - 1:
        break
    if connected.find(edge[0][0]) != connected.find(edge[0][1]):
        connected.unite(edge[0][0], edge[0][1])
        eu += 1
        res = poses[edge[0][0]][0] * poses[edge[0][1]][0]
    else:
        print("no")

print(res)
submit(res, year=2025, day=8, part='b')
