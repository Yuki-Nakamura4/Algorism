# 3つあるうちの2つが決まれば1つは自動的に求まるという性質を利用して、全探索を行う
# これによりO(N^3)の計算量がO(N^2)に削減される
N , K = map(int, input().split())

count = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if 1 <= K - (i + j )  <= N:
            count += 1

print(count)