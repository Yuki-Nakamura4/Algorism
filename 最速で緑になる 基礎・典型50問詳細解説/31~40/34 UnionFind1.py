# UnionFindは、グラフの頂点の連結(Union)と2頂点が連結かを確認する処理(Find)を高速で行えるデータ構造
# 実装は難しいのでクラスを丸々コピペして使う


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1] * n

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


# 入力の受け取り
N, Q = map(int, input().split())

# UnionFindを用意
UF = UnionFind(N + 1)

# Q回
for i in range(Q):
    # 入力の受け取り
    P, A, B = map(int, input().split())

    # P=0の場合
    if P == 0:
        # A,Bを連結
        UF.merge(A, B)

    # P=1の場合
    else:
        # A,Bが連結なら
        if UF.same(A, B):
            # 「Yes」を出力
            print("Yes")
        # 連結でないなら
        else:
            # 「No」を出力
            print("No")
