N, L = map(int, input().split())
A = list(map(int, input().split()))


# んしょ......んしょ......
ans = 0

for i in range(N):
    if A[i] >= L:
        ans += 1

print(ans)

# 模範解答
N, L = map(int, input().split())
A = list(map(int, input().split()))
print(len(list(filter(lambda x: x >= L, A))))
