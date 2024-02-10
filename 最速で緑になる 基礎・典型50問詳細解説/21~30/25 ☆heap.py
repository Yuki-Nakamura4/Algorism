# 入力の受け取り
N, K = map(int, input().split())
P = list(map(int, input().split()))

# heapqのインポート
import heapq

# (1)heap queueを用意する
que = []

# (2)P1~PKをheap queueへ入れる
for i in range(K):
    heapq.heappush(que, P[i])

# (3)heap queueの最小値を出力する
print(que[0])

# i=K~(N-1)
for i in range(K, N):
    # (4)heap queueから最小値を取り出す
    x = heapq.heappop(que)
    # (5)(heap queueの最小値)とPiのうち大きい方をheap queueへ戻す
    heapq.heappush(que, max(x, P[i]))
    # (6)(heap queueの最小値)を出力する
    print(que[0])
    # (7)次のiへ((4)へ戻る)
