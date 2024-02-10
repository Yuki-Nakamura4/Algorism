# 模範回答

import sys

N, M = map(int, input().split())
S = list(input())
T = input()
# 再帰の上限を増やす
sys.setrecursionlimit(2 * N + 99)

# 文字列Sの長さ分探索済みかどうかを表すリスト
used = [False] * N

# 文字列Sのpos番目からM文字が文字列Tと一致するかどうかを調べる関数
# posはposition、文字列Sの何文字目から調べるかを表す
def match(pos):
    # pos番目からM文字が文字列Tと一致するかどうかを調べる
    for i in range(pos, pos + M):
        # 文字列Sの長さを超えてしまった場合や、
        # 文字列Sのi番目の文字が文字列Tのi - pos番目の文字と一致しない場合は、
        # Falseを返す
        if i < 0 or i >= N or S[i] != "?" and S[i] != T[i - pos]:
            return False
    return True


def dfs(pos):
    used[pos] = True
    S[pos : pos + M] = "?" * M
    for i in range(pos - M + 1, pos + M):
        # 文字列Sのi番目からM文字が文字列Tと一致し、かつ文字列Sのi番目がまだ探索済みでない場合は、
        # 再帰的にdfs()を呼び出す
        if match(i) and not used[i]:
            dfs(i)

# 文字列Sを前から順番に探索する
for i in range(N):
    # もし文字列Sのi番目からM文字が文字列Tと一致し、かつ文字列Sのi番目がまだ探索済みでない場合は、
    if match(i) and not used[i]:
        # 再帰的にdfs()を呼び出す
        dfs(i)
# すべての文字が"?"になっていたら、"Yes"を出力する
print("Yes" if all(c == "?" for c in S) else "No")
