N, X = map(int, input().split())
S = list(map(int, input().split()))

# ans = 0

# for i in range(len(S)):
#     if S[i] <= X:
#         ans += S[i]

# print(ans)

# 模範解答
print(sum(filter(lambda x: x <= X, S)))

# filter関数は、第一引数に関数、第二引数にリストをとり、
# 第二引数のリストの要素を第一引数の関数に入れてTrueになるものだけを返す

# lambda関数は、無名関数を作るためのもの
# lambda 引数: 処理
# という形で書く
# 例えば、
# def func(x):
#     return x + 1
# という関数を
# lambda x: x + 1
# と書ける
