H, W, N = map(int, input().split())

grid = ["." * W for _ in range(H)]

x, y = 0, 0
direction = 0


def rotate_clockwise(x, y):
    global direction
    direction = (direction + 1) % 4


def rotate_counter_clockwise():
    global direction
    direction = (direction - 1) % 4


def move():
    global x, y, direction
    if direction == 0:
        x = (x - 1) % H
    elif direction == 1:
        y = (y + 1) % W
    elif direction == 2:
        x = (x + 1) % H
    else:
        y = (y - 1) % W


for _ in range(N):
    if grid[x][y] == ".":
        grid[x][y] = "#"
        rotate_clockwise()
    else:
        grid[x][y] = "."
        rotate_counter_clockwise()
    move()

# グリッドの状態を出力する
for row in grid:
    print("".join(row))
