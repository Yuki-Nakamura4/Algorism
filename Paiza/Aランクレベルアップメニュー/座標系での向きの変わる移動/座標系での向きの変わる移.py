# X, Y, N = map(int, input().split())
# directions = [input() for _ in range(N)]

# now_direction = "N"

# # 各方角の左と右の方角を辞書で表現
# direction_change = {
#     'N': {'L': 'W', 'R': 'E'},
#     'E': {'L': 'N', 'R': 'S'},
#     'S': {'L': 'E', 'R': 'W'},
#     'W': {'L': 'S', 'R': 'N'}
# }

# # 各方向に移動したときの座標変化を辞書で表現
# move_change = {
#     'N': {'L': (-1, 0), 'R': (1, 0)},
#     'E': {'L': (0, -1), 'R': (0, 1)},
#     'S': {'L': (1, 0), 'R': (-1, 0)},
#     'W': {'L': (0, 1), 'R': (0, -1)}
# }

# for d in directions:
#     dx, dy = move_change[now_direction][d]
#     X += dx
#     Y += dy
    
#     now_direction = direction_change[now_direction][d]

#     print(X, Y)

# 模範解答
# こちらの方が簡潔
# 方角をインデックスで表現し、右なら+1、左なら+3して、4で割った余りを求める
x, y, n = map(int, input().split())
directions = ["N", "E", "S", "W"]
now_direction = 0

for _ in range(n):
    lr = input()
    if lr == "L":
        now_direction = (3 + now_direction) % 4
    else:
        now_direction = (1 + now_direction) % 4

    if directions[now_direction] == "N":
        y -= 1
    elif directions[now_direction] == "E":
        x += 1
    elif directions[now_direction] == "S":
        y += 1
    elif directions[now_direction] == "W":
        x -= 1

    print(x, y)