P = list(map(int, input().split()))
N =int(input())
points = []
[points.append(list(map(int, input().split()))) for _ in range(N)]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclid(a,b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

manhattan_distances = []
euclid_distances = []

for i in range(N):
    manhattan_distances.append([manhattan(P, points[i]), i])
    euclid_distances.append([euclid(P, points[i]), i])

manhattan_distances.sort()
euclid_distances.sort()

for i in range(3):
    print(euclid_distances[i][1]+1)

for i in range(3):
    print(manhattan_distances[i][1]+1)