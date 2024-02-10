# 入力の受け取り
N = int(input())
S = input()

# deque のインポート
from collections import deque

# キューを用意
que = deque()

# 逆順で考えるため、最初にNを追加
que.append(N)

# i=(N-1)~0 -1ずつ
for i in range(N - 1, -1, -1):
    # Sのi文字目が「R｣
    if S[i] == "R":
        # 先頭(左端)へ「i」を追加
        que.appendleft(i)
    # そうでない場合(Sのi文字目が「L」)
    else:
        # 末端(右端)へ「i」を追加
        que.append(i)

# 答えの出力
# ([]がいらない場合は先頭に「*」をつける)
print(*que)
