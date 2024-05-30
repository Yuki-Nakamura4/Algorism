N = int(input())
A = list(map(int, input().split()))

# 3つの整数の組み合わせを全探索
Answer = False
for i in range(N):
	for j in range(i+1, N): # i+1から始めることで、iと同じものを選ばないようにし、かつ重複を避ける
		for k in range(j+1, N): # j+1から始めることで、jと同じものを選ばないようにし、かつ重複を避ける
			if A[i] + A[j] + A[k] == 1000:
				Answer = True

# 出力
if Answer == True:
	print("Yes")
else:
	print("No")