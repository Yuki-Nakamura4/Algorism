# 自分の解答
# Y, X, D = input().split()
# Y , X = int(Y), int(X)  
# d = input()

# if d == "R":
#     if D == "N":
#         X +=  1
#     elif D == "E":
#         Y += 1
#     elif D == "S":
#         X -= 1
#     elif D == "W":
#         Y -= 1
# elif d == "L":
#     if D == "N":
#         X -= 1
#     elif D == "E":
#         Y -= 1
#     elif D == "S":
#         X += 1
#     elif D == "W":
#         Y += 1

# print(Y, X)

# 模範解答
# あらかじめ、右に移動するときの座標の変化を考えておけば、
# 左に移動するときは、-1*(右に移動するときの座標の変化)で求められる
y, x, now_direction = input().split()
y = int(y)
x = int(x)
d = input()
lr = 1

if d == "L":
    lr = -1

if now_direction == "N":
    x += lr
elif now_direction == "E":
    y += lr
elif now_direction == "S":
    x -= lr
elif now_direction == "W":
    y -= lr

print(y, x)