# 竜の問題

# 模範解答
# 先頭の位置だけ記録してその軌道を使えば良い

N, Q = map(int, input().split())

p = [(i, 0) for i in range(N, 0, -1)]
x, y = 1, 0
for _ in range(Q):
    T, C = input().split()
    if T == "1":
        if C == "R":
            x += 1
        elif C == "L":
            x -= 1
        elif C == "U":
            y += 1
        elif C == "D":
            y -= 1
        p.append((x, y))
    else:
        print(*p[-int(C)])


# アホの解き方。TLEになる。

N, Q = map(int, input().split())

from collections import deque

que = deque()

for i in range(1, N + 1):
    que.append(i)
    que.append(0)

for q in range(Q):
    values = input().split()

    if values[0] == "1":
        if values[1] == "R":
            x = que.popleft()
            y = que.popleft()
            new_x = x + 1
            new_y = y
            que.appendleft(y)
            que.appendleft(x)
            que.pop()
            que.pop()
            que.appendleft(new_y)
            que.appendleft(new_x)
        elif values[1] == "L":
            x = que.popleft()
            y = que.popleft()
            new_x = x - 1
            new_y = y
            que.appendleft(y)
            que.appendleft(x)
            que.pop()
            que.pop()
            que.appendleft(new_y)
            que.appendleft(new_x)
        elif values[1] == "U":
            x = que.popleft()
            y = que.popleft()
            new_x = x
            new_y = y + 1
            que.appendleft(y)
            que.appendleft(x)
            que.pop()
            que.pop()
            que.appendleft(new_y)
            que.appendleft(new_x)
        elif values[1] == "D":
            x = que.popleft()
            y = que.popleft()
            new_x = x
            new_y = y - 1
            que.appendleft(y)
            que.appendleft(x)
            que.pop()
            que.pop()
            que.appendleft(new_y)
            que.appendleft(new_x)
    else:
        p = int(values[1])
        ans_list = list(que)
        print(str(ans_list[p * 2 - 2]) + " " + str(ans_list[p * 2 - 1]))


# 模範解答
