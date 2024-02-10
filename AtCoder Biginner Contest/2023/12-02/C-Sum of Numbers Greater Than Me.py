# Counterは辞書型のサブクラスで、要素をカウントするのに便利
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# カウンターを使って、Aの要素をカウント
# たとえば、A = [1, 2, 3, 1, 2, 1]のとき、
# c = Counter(A)とすると、
# c = {1: 3, 2: 2, 3: 1}となる
c = Counter(A)

# 答えを格納する辞書型の変数
ans = {}
# sは累積和
s = 0
# c.items()は、cの要素を(要素, 個数)のタプルで返す
# たとえば、c = {10: 1, 50: 2, 20: 3}のとき、
# c.items()は、[(10, 1), (50, 2), (20, 3)]を返す
# sorted(c.items(), reverse=True)は、
# [{50: 2}, {20: 3}, {10: 1}]を返す
for v, t in sorted(c.items(), reverse=True):
    # vは要素、tは個数
    ans[v] = s
    # 累積和を更新
    s += v * t

# 答えを出力
# for x in Aは、Aの要素を順番にxに代入する
# ans[x]は、xをキーとする辞書型の値を返す
# つまり、ans[x]は、xの累積和を返す
# これを、Aの要素を順番に出力することで、
# Aの要素の累積和を出力することができる
print(" ".join(str(ans[x]) for x in A))

# N = int(input())
# A = list(map(int, input().split()))

# num_list = [0] * (10**6 + 1)
# ans = 0

# for i in range(len(A)):
#     num_list[A[i]] += 1

# for i in range(len(A)):
#     for j in range(A[i] + 1, N):
#         ans += j * num_list[j]
#     print(ans)
#     ans = 0
