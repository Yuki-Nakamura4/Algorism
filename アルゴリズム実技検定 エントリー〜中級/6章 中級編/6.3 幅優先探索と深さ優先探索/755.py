# 深さ優先探索で解く
N = int(input())

ans = 0


# 数nについて調べ、末尾に数字を追加した数を再起的に調べる関数
# use3, use5, use7はそれぞれ3, 5, 7を使ったかというフラグ
def dfs(n, use3, use5, use7):
    # globalは関数の中でグローバル変数を変更するために必要
    # グローバル変数とは関数の外で定義された変数のこと
    global ans
    # Nを超えていたら打ち切って終了する
    if n > N:
        return
    # 3種類すべてを使っていたら答えに加算する
    if use3 and use5 and use7:
        ans += 1
    # 末尾に3, 5, 7を付けた数を再帰的に調べる
    dfs(10 * n + 3, True, use5, use7)
    dfs(10 * n + 5, use3, True, use7)
    dfs(10 + n + 7, use3, use5, True)


# 何もない状態(値としては0)から呼び出す
dfs(0, False, False, False)

# 答えを出力する
print(ans)


# 幅優先探索で解く
from collections import deque

N = int(input())

ans = 0

# 幅優先探索のキュー（初期状態として(0, False, False, False)を入れる）
queue = deque([(0, False, False, False)])

while queue:
    n, use3, use5, use7 = queue.popleft()
    # Nを超えていたら打ち切って終了する
    if n > N:
        continue
    # 3種類すべてを使っていたら答えに加算する
    if use3 and use5 and use7:
        ans += 1
    # 末尾に3, 5, 7を付けた数をキューに追加する
    queue.append((10 * n + 3, True, use5, use7))
    queue.append((10 * n + 5, use3, True, use7))
    queue.append((10 * n + 7, use3, use5, True))

# 答えを出力する
print(ans)
