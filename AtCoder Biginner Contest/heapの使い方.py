# 使いどころ：最小値・最大値を高速に取り出したいとき

# インポート：import heapq
import heapq

# リストを用意
que = list()

# リストのheap化【O(N)】：heapify(リスト)
heapq.heapify(que)

# 要素の追加【O(logN)】：heappush(リスト,要素)
heapq.heappush(que, 6)
heapq.heappush(que, 1)

# 最小値の参照【O(1)】：リスト[0]
print(que[0])

# 最小値の取り出し【O(logN)】：heappop(リスト)
# ※最小値を取り出すとその要素は削除される
minX = heapq.heappop(que)
