N, X, K = map(int, input().split())
count = (K- 4*N) // 4
result=count * X * 2
if (K-4*N) % 4 == 3:
	result += X
print(result)