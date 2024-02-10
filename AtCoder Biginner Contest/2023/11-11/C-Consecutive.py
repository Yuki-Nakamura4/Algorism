N, Q = map(int, input().split())
S = input()

# TLEになる
# l = [0] * Q
# r = [0] * Q

# for i in range(1, Q + 1):
#     l[i - 1], r[i - 1] = map(int, input().split())

# count = 0

# for i in range(1, Q + 1):
#     for j in range(l[i - 1], r[i - 1]):
#         if S[j - 1] == S[j]:
#             count += 1
#     print(count)
#     count = 0

# 模範解答
# 累積和を使う
# 累積和とは、ある数列の各要素の和を順番に足していった数列のこと
# 例えば、数列A = [1, 2, 3, 4]の累積和は、
# [1, 3, 6, 10]となる

# 事前に同じ文字が隣り合っている箇所を数え上げる
count = [0] * N
for i in range(1, N):
    # count[i]には、S[0]からS[i]までの文字列の中で、
    # 同じ文字が隣り合っている箇所の数が入る
    # 例えば、S = "11011"のとき、
    # count = [0, 1,　1 , 1, 2]となっている
    # ここで、S[i - 1] == S[i]は、S[i - 1]とS[i]が同じ文字かどうかを調べている
    count[i] = count[i - 1] + (S[i - 1] == S[i])

# 各クエリの処理
for i in range(Q):
    l, r = map(int, input().split())

    # クエリ内で同じ文字が隣り合っている箇所を数え上げる
    # 例えば、S = "11011"のとき、
    # count = [0, 1, 1, 2, 2]となっている
    # このとき、l = 2, r = 4とすると、
    # count[r - 1] - count[l - 1] = 2 - 1 = 1となる
    result = count[r - 1] - count[l - 1]

    print(result)
