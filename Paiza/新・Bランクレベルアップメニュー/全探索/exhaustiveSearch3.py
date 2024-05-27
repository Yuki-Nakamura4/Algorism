# 自分の解答
N = int(input())
X = [int(input()) for _ in range(N)]

INF = 10**10 # 十分に大きい数で初期化
ans = INF

def plus_one(num):
    return num+1

def minus_one(num):
    return num-1

def set_prev_one(num):
    return int("1" + str(num))

def set_after_one(num):
    return int(str(num) + "1")

def default(num):
    return num

methods = [plus_one, minus_one, set_prev_one, set_after_one, default] # 何も操作しない場合を忘れない

for i in X:
    for j in X:
        if i == j:
            continue
        for method in methods:
            new_i = method(i)
            for method in methods:
                new_j = method(j)
                result = abs(new_i - new_j)
                ans = min(ans, result)

print(ans)


# # 模範解答
# # 関数名がsousaなのはいかがなものか......
# # 関数1つにまとめている分シンプルで見やすい。
# # ただ操作の内容がパッとわからないという意味での可読性や変更時の保守性は自分の解答の方が良さそう
# def sousa(number, pat):
#     if pat == 0:
#         return number
#     elif pat == 1:
#         return number+1
#     elif pat == 2:
#         return number-1
#     elif pat == 3:
#         return number+10**len(str(number))
#     else:
#         return number*10+1

# N = int(input())
# X = []
# for i in range(N):
#     X.append(int(input()))
# ans = 10**8
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(5):
#             for l in range(5):
#                 ans = min(ans, abs(sousa(X[i], k)-sousa(X[j], l)))
# print(ans)