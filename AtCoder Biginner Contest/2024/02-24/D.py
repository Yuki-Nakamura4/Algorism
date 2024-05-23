import itertools

N = int(input())
A = list(map(int, input().split()))

for p in itertools.combinations(range(N), ):
    print(p)
