# # 自分の解答
# 最初の2行が無駄。文字列で受け取る方が良い。
# X = int(input())
# S = str(X)
# ans = 0

# for i in range(4):
#     start = i * 8 
#     partial_num = int(S[start: start + 8])
#     ans += partial_num

# print(ans)

# 模範解答
# 文字列で受け取る
X = input()

ans = 0

for i in range(4):
    ans += int(X[8 * i: 8 * (i + 1)])

print(ans)