N = int(input())
D = list(map(int, input().split()))

ans = 0

# 愚直解
# for i in range(1, N+1):
#     for j in range(1, D[i-1]+1):
#         if len(str(i)) >= 2 and len(str(j)) >= 2:
#             if i == j and i%10 == i//10:
#                 ans += 1
#         elif len(str(i)) >= 2 and len(str(j)) == 1:
#             if i%10 == j and i//10 == j:
#                 ans += 1
#         elif len(str(i)) == 1 and len(str(j)) >= 2:
#             if i == j%10 and i == j//10:
#                 ans += 1
#         else:
#             if i == j:
#                 ans += 1

# 模範解答
for i, d in enumerate(D):
    month_str = str(i + 1)
    for x in range(d):
        day_str = str(x + 1)
        # 連結した文字列の中に重複がないかを調べている
        # set関数を使うことで、重複を取り除くことができる
        if len(set(month_str + day_str)) == 1:
            ans += 1

# enumerate関数は、リストの要素とインデックスを同時に取得できる
# 例えば、
# for i in range(len(D)):
#     print(i, D[i])
# と書くと、
# 0 1
# 1 2
# 2 3
# と出力されるが、
# for i, d in enumerate(D):
#     print(i, d)
# と書くと、
# 0 1
# 1 2
# 2 3
# と出力される
# つまり、iにはインデックスが、dには要素が入る
# 今回の場合、iには月、dには日が入る

# set関数は、リストの要素を重複なく取り出す
# 例えば、
# A = [1, 1, 2, 3, 3]
# print(set(A))
# と書くと、
# {1, 2, 3}
# と出力される
# つまり、今回の場合、月と日の数字が重複しているかどうかを調べている
# 例えば、
# month_str = "1"
# day_str = "1"
# とすると、
# set(month_str + day_str)
# は、
# {"1"}
# となる
# つまり、月と日の数字が重複している
# 例えば、
# month_str = "1"
# day_str = "2"
# とすると、
# set(month_str + day_str)
# は、
# {"1", "2"}
# となる
# つまり、月と日の数字が重複していない

print(ans)
