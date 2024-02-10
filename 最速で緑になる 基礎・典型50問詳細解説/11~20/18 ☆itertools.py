S, K = map(str, input().split())
K = int(K)

# 作れる文字列を格納するセット
Sset = set()

import itertools

for p in itertools.permutations(S):
    # タプルを結合して文字列にし、セットに追加
    Sset.add("".join(p))

# セットをリストに変換
Slist = list(Sset)

# ソート
Slist.sort()

# K番目の文字列を出力
print(Slist[K - 1])
