N = int(input())

A = list(map(int, input().split()))

Slist = []
Tlist = []

for i in range(N - 1):
    S, T = map(int, input().split())
    Slist.append(S)
    Tlist.append(T)

for i in range(N - 1):
    if Slist[i] == 0:
        continue
    while A[i] >= Slist[i]:
        A[i + 1] += Tlist[i]
        A[i] -= Slist[i]

print(A[-1])


# 模範解答
# N = int(input())
# A = list(map(int, input().split()))
# for i in range(N - 1):
#     S, T = map(int, input().split())
#     A[i+1] += A[i] // S * T
# print(A[-1])
