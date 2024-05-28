# # 自分の解答
# X, M, N = map(int, input().split())

# for i in range(1,N+1):
#     rnd = 0
#     for j in range(i, 0, -1):
#         rnd += (X**j)
#     rnd = rnd % M
#     print(rnd)

#　模範解答
X, M, N = map(int, input().split())
pow = 1
seed = 0

for i in range(N):
    pow *= X
    pow %= M
    seed += pow
    seed %= M
    print(seed)