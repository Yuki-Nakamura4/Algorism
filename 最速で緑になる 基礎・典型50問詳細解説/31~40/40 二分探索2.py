# pypyで提出

# 入力の受け取り
N = int(input())
A = list(map(int, input().split()))

# 1,2,3,...が何番目にあるかの記録 左端には「0」を入れておく
Aindx = [[0] for i in range(10**6)]

# i=0~(N-1)
for i in range(N):
    # インデックス番号を記録
    # 1インデックスなので「i+1」を記録することに注意
    Aindx[A[i]].append(i + 1)

# i=0~(N-1)
for i in range(10**6):
    # 右端に∞=10^6を追加
    Aindx[i].append(10**6)


# Xがあるインデックス番号のうちL以上で最小のもの
def NibutanLeft(X, L):
    l = 0
    r = len(Aindx[X]) - 1

    while 1 < r - l:
        c = (l + r) // 2

        # 左または右を更新する
        if L <= Aindx[X][c]:
            r = c
        else:
            l = c

    return r


# Xがあるインデックス番号のうちR以下で最大のもの
def NibutanRight(X, R):
    l = 0
    r = len(Aindx[X]) - 1

    while 1 < r - l:
        c = (l + r) // 2

        if Aindx[X][c] <= R:
            l = c
        else:
            r = c

    return l


Q = int(input())

for i in range(Q):
    L, R, X = map(int, input().split())

    # 「Xがあるインデックス番号のうちL以上で最小のもの」
    Lindx = NibutanLeft(X, L)
    # 「Xがあるインデックス番号のうちR以下で最大のもの」
    Rindx = NibutanRight(X, R)
    # 答えを出力
    print(Rindx - Lindx + 1)


# # 別解
# # 入力の受け取り
# N = int(input())
# A = list(map(int, input().split()))

# # 1,2,3,...が何番目にあるかの記録 左端には「0」を入れておく
# Aindx = [[0] for i in range(10**6)]

# # i=0~(N-1)
# for i in range(N):
#     # インデックス番号を記録
#     # 1インデックスなので「i+1」を記録することに注意
#     Aindx[A[i]].append(i + 1)

# # i=0~(N-1)
# for i in range(10**6):
#     # 右端に∞=10^6を追加
#     Aindx[i].append(10**6)

# # 入力の受け取り
# Q = int(input())

# # bisectをインポート
# import bisect

# # Q回
# for i in range(Q):
#     # 入力の受け取り
#     L, R, X = map(int, input().split())

#     # Lを大小関係を保ったままリストに挿入する位置のインデックス(同じ数があれば左側へ)
#     Lindx = bisect.bisect_left(Aindx[X], L)
#     # Rを大小関係を保ったままリストに挿入する位置のインデックス(同じ数があれば右側へ)
#     Rindx = bisect.bisect_right(Aindx[X], R)
#     # 答えを出力
#     print(Rindx - Lindx)
