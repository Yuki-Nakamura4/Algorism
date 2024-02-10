# 分からなかった

N, M = map(int, input().split())
A = list(map(int, input().split()))

# # 得票数を格納するリスト
# # このリストのi番目の要素には、i + 1番目の候補者の得票数が入る
# vote = [0] * N

# # 当選者の番号を格納する変数
# winner = 0

# max_vote = 0

# for a in A:
#     vote[a - 1] += 1
#     # voteの各要素を見て、最大値のうちいちばん左にあるものを当選者とする
#     for i in vote:
#         if vote[i] > max_vote:
#             max_vote = vote[i]
#             winner = i + 1
#     print(winner)

# 模範解答

# 得票数を格納するリスト
v = [0] * (N + 1)
# 現在の最多得票数の候補者の番号
top = 0

for x in A:
    v[x] += 1
    # v[x]が現在の最多得票数よりも大きいか、
    # v[x]が現在の最多得票数と等しく、xがtopよりも小さいかを調べる
    # このとき、topをxに更新する
    if v[x] > v[top] or v[x] == v[top] and x < top:
        top = x
    print(top)
