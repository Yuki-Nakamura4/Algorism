# わからなかった

# import math

# D = int(input())

# # (x+y)の目星をつける
# rtD = int(math.ceil((math.sqrt(D))))

# # 答えを格納する変数
# ans = float("inf")

# # xとyの組み合わせを列挙し、答えを更新する
# for i in range(rtD, rtD + 100):
#     for x in range(rtD + 1):
#         ans = min(abs(ans), abs(rtD**2 - 2 * x * (rtD - x) - D))
#     rtD += 1

# print(ans)

# 模範解答
D = int(input())
ans = D

for x in range(int(D**0.5) + 9):
    # x**2 + y**2 = D　に最も近いxとyを求める
    # zは理想的なy座標。ただし整数ではない
    # 問題で求めたいyは整数なので、zに最も近い整数を求める
    z = D - x**2
    if z < 0:
        ans = min(ans, -z)
    else:
        y1 = int(z**0.5)  # 半径の内側の整数
        y2 = y1 + 1  # 半径の外側の整数
        # y1 * y1 <= z < y2 * y2
        ans = min(ans, z - y1 * y1, y2 * y2 - z)
print(ans)
