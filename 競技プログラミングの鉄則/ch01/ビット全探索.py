# ビット全探索のコード
# N枚のカードから一部を選択し、カードに書かれた数の合計をKにできるかどうか判定する
N , K = map(int, input().split())

# N枚のカードの数字を入力
A = list(map(int, input().split()))

# 2^N通りの全探索
for i in range(1<<N):
    sum = 0
    for j in range(N):
        if i & (1<<j):
            sum += A[j]
    if sum == K:
        print("Yes")
        exit()
