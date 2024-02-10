N = int(input())
S = input()

# 文字列Sの種類
set_S = set(S)

# 答えを格納する変数
ans = 0

for s in set_S:
    num = 0
    max_num = 0

    for i in range(N):
        if S[i] == s:
            num += 1
            max_num = max(max_num, num)
        else:
            num = 0

    ans += max_num

print(ans)

# 模範解答

import collections
import itertools

N = int(input())
S = input()

# 辞書型の変数に、文字列Sの各文字の個数を格納する
dict = collections.defaultdict(int)

for c, g in itertools.groupby(S):
    # 現在の辞書の値と、現在の文字列の個数のうち、大きい方を辞書に格納する
    dict[c] += max(dict[c], len(list(g)))
# 辞書の値の合計を出力する
print(sum(dict.values()))

# dexaultdictは、辞書型のサブクラスで、辞書型のget()メソッドに似たメソッドを持つ
# このメソッドは、辞書に存在しないキーを指定した場合に、
# そのキーと引数で指定した値を辞書に追加する
# 例えば、d = defaultdict(int)とすると、
# d[1] = 0となる
# また、d = defaultdict(str)とすると、
# d[1] = ""となる

# itertools.groupby()は、リストや文字列などの連続した要素をまとめてくれる関数
# 例えば、S = "11011"のとき、
# for c, g in itertools.groupby(S)とすると、
# c = "1", g = ["1", "1"]
# c = "0", g = ["0"]
# c = "1", g = ["1", "1"]
# となる
# このとき、d = collections.defaultdict(int)とすると、
# d["1"] += max(d["1"], len(list(g)))となり、
# d["1"] = 0 + max(0, 2) = 2となる
# このとき、d["0"] = 0となる
