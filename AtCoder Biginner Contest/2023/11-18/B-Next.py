N = int(input())
A = list(map(int, input().split()))

# 結果はset_Aを降順にソートしたものの2番目
result = sorted(set(A), reverse=True)[1]

print(result)
