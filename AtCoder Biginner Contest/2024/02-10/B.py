Q = int(input())

A = list(map(int, input().split()))

for i in range(Q):
    query = map(int, input().split())
    if query[0] == 1:
        A.append(query[1])
    else:
        print(A[-query[1]])

# 模範解答
# Q = int(input())
# A = []
# for _ in range(Q):
#     t, x = map(int, input().split())
#     if t == 1:
#         A.append(x)
#     else:
#         print(A[-x])
