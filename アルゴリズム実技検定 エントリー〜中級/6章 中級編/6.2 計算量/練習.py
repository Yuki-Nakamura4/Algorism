# O(N+M)のアルゴリズム

# 各数が含まれている個数を保持する辞書
count = {}

for i in range(0, N):

    # もしcountにA[i]の個数がなければ0で初期化する
    if A[i] not in count:
        count[A[i]] = 0
    
    # A[i]の個数を加算する
    count[A[i]] += 1

# 1以上M未満の各iについて数えた個数を出力する
for i in range(0, M):

    if i not in count:
        print(0)
    else:
        print(count[i])