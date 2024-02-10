# 使いどころ: 幅優先探索

# インポート
from collections import deque

# 作成：変数名=deque()
que = deque()

# 先頭(左端)に要素追加【O(1)】：変数名.appendleft(要素)
que.appendleft(1)

# 末尾(右端)に要素追加【O(1)】：変数名.append(要素)
que.append(3)

# 先頭(左端)から要素を取り出して削除【O(1)】：変数名.popleft()
x = que.popleft()

# 末尾(右端)から要素を取り出して削除【O(1)】：変数名.pop()
y = que.pop()
