# 入力の受け取り
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# i番目のすぬけ君が初めて宝石をもらう時間
# 初期値は大きい数
time = [10**15] * N

# 1週目
for i in range(N):
    # 次のすぬけ君の番号。i=N-1のとき、次のすぬけ君の番号=Nではなく=0とするためNで割った余りを取る
    next = (i + 1) % N
    # 高橋君からもらうのが早いか、隣のすぬけ君からもらうのが早いか
    time[next] = min(T[next], time[i] + S[i])

# 2周目(N-1番目から0番目への部分をうまく処理するためにもう1周する)
for i in range(N):
    next = (i + 1) % N
    # 1周目で計算した時間が早いか、隣のすぬけ君からもらうのが早いか
    time[next] = min(time[next], time[i] + S[i])

# 答えの出力
for i in range(N):
    print(time[i])


# ダイクストラ法でも解けるらしい
import heapq

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# 各すぬけ君が初めて宝石をもらう時間を保存するリスト
time = [float("inf")] * N

# ダイクストラ法のための優先度付きキュー
queue = []

# 初期化：各すぬけ君が高橋君から宝石をもらう時間を設定
for i in range(N):
    time[i] = T[i]
    heapq.heappush(queue, (T[i], i))

# ダイクストラ法
while queue:
    cur_time, cur_i = heapq.heappop(queue)
    if cur_time > time[cur_i]:
        continue
    next_i = (cur_i + 1) % N
    next_time = cur_time + S[cur_i]
    if next_time < time[next_i]:
        time[next_i] = next_time
        heapq.heappush(queue, (next_time, next_i))

# 答えの出力
for i in range(N):
    print(time[i])
