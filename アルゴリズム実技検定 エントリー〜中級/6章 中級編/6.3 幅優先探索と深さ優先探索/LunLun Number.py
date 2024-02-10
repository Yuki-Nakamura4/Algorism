K = int(input())

from collections import deque

# ルンルン数を格納するキュー
queue = deque()
for i in range(1, 10):
    queue.append(i)

# K番目のルンルン数
ans = 0

# K番目のルンルン数を求める
for i in range(K):
    # キューの先頭を取り出す
    ans = queue.popleft()

    # 取り出した数の末尾が0であれば、末尾に0を付けた数と末尾に1を付けた数をキューに追加する
    if ans % 10 == 0:
        queue.append(ans * 10)
        queue.append(ans * 10 + 1)

    # 取り出した数の末尾が9であれば、末尾に8を付けた数と末尾に9を付けた数をキューに追加する
    elif ans % 10 == 9:
        queue.append(ans * 10 + 8)
        queue.append(ans * 10 + 9)

    # 先頭の末尾が0でも9でもなければ、末尾に1小さい数、末尾の数、1大きい数を付けた数をそれぞれキューに追加する
    else:
        queue.append(ans * 10 + ans % 10 - 1)
        queue.append(ans * 10 + ans % 10)
        queue.append(ans * 10 + ans % 10 + 1)

# K番目のルンルン数を出力する
print(ans)
