# 模範解答
# 計算量はO(Q) + O(N)

N = int(input())
S = input()
Q = int(input())

# 辞書内包表記。キーも値もアルファベットの辞書を作成
m = {x: x for x in "abcdefghijklmnopqrstuvwxyz"}

# O(Q)
for _ in range(Q):
    c, d = input().split()
    for k, v in m.items():  # mのキーと値を取り出す
        if v == c:
            m[k] = d

# O(N)
print("".join(m[c] for c in S))


# 遅すぎる
from collections import defaultdict

N = int(input())
S = input()
Q = int(input())

char_dict = defaultdict(list)

# O(N)
for i in range(N):
    char_dict[S[i]].append(i)

# ここが遅い。最悪の計算量はO(NQ) NもQも最大2*10^5なので、10^10回の計算が必要
for i in range(Q):
    c, d = input().split()
    if c == d:
        continue
    char_dict[d].extend(char_dict[c])  # 計算量はO(len(char_dict[c]))つまりO(N)
    char_dict[c] = []

# O(N)
result = [""] * N

# O(N)
for key, value in char_dict.items():
    for element in value:
        result[element] = key

ans = "".join(result)
print(ans)
