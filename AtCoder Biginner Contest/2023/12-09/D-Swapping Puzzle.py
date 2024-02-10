# 模範解答
from collections import deque
from copy import deepcopy


# なぜタプルにするのか↓
# タプルはハッシュ可能であり、辞書のキーとして使える
# 一方、リストはハッシュ不可能であり、辞書のキーとして使えない
def to_tuple(a):
    return tuple(tuple(r) for r in a)


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

d = {to_tuple(A): 0}
# qは探索すべき2次元配列を格納する
# 初期状態の配列Aから探索を始めるため、qにAを格納する
q = deque([A])

# 幅優先探索
# qが空になるまで続ける
while len(q) > 0:
    a = q.popleft()
    for i in range(H - 1):
        # deepcopyは、リストの要素をコピーする
        # たとえば、a = [[1, 2], [3, 4]]とすると、
        # b = deepcopy(a)は、b = [[1, 2], [3, 4]]となる
        # 一方、b = aとすると、b = [[1, 2], [3, 4]]となる
        # しかし、a[0][0] = 5とすると、b = [[5, 2], [3, 4]]となる
        # これは、b = aとすると、aとbは同じオブジェクトを参照するためである
        # つまり、b = aとすると、aの要素を変更すると、bの要素も変更される
        # これを防ぐために、deepcopyを使う
        b = deepcopy(a)
        b[i], b[i + 1] = b[i + 1], b[i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            q.append(b)
    for j in range(W - 1):
        b = deepcopy(a)
        for i in range(H):
            b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            q.append(b)

print(d[to_tuple(B)] if to_tuple(B) in d else -1)
