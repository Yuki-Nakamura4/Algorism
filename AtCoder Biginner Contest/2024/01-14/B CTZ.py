# 模範解答

N = int(input())

print(bin(N)[::-1].find("1"))

# [::-1]で文字列を逆順にする
# find()はシーケンス型のメソッドで、引数に指定した文字列が見つかった場合はそのインデックスを返し、見つからなかった場合は-1を返す


# N = int(input())

# binary = bin(N)

# ans = 0

# for i in range(-1, -len(binary) - 1, -1):
#     if binary[i] == "0":
#         ans += 1
#     else:
#         break

# print(ans)
