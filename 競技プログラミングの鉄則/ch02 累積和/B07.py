D = int(input())
N = int(input())
L, R = [None]*N,  [None]*N
for i in range(N):
    L[i], R[i] = map(int, input().split())