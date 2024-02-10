from collections import deque

N = int(input())

grid = [["#" for _ in range(N + 2)] for _ in range(N + 2)]

P = []

for i in range(1, N + 1):
    S = input()
    for j in range(N):
        if S[j] == "#":
            grid[i][j + 1] = "#"
        elif S[j] == ".":
            grid[i][j + 1] = "."
        else:
            grid[i][j + 1] = "."
            P.append((i, j + 1))


def move(x, y, direction):
    if direction == 0:
        if grid[x - 1][y] != "#":
            x -= 1
    elif direction == 1:
        if grid[x][y - 1] != "#":
            y -= 1
    elif direction == 2:
        if grid[x + 1][y] != "#":
            x += 1
    elif direction == 3:
        if grid[x][y + 1] != "#":
            y += 1
    return (x, y)


Q = deque()
Q.append((P[0], P[1]))
visited = set((P[0], P[1]))

count = 0

while Q:
    for _ in range(len(Q)):
        players = Q.popleft()
        if players[0] == players[1]:
            print(count)
            exit()

        for i in range(4):
            newP0 = move(players[0][0], players[0][1], i)
            newP1 = move(players[1][0], players[1][1], i)
            if (newP0, newP1) not in visited:
                Q.append((newP0, newP1))
                visited.add((newP0, newP1))

    count += 1

print(-1)
