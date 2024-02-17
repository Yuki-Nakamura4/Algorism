S = "ABCDE"

rS = ""

for i in range(-1, -1, -1):
    rS += S[i]

print(rS)

# insertを使う
S = "ABCDE"

list = []

for i in range(len(S)):
    list.insert(0, S[i])

print("".join(list))


# dequeを使う
from collections import deque

S = "ABCDE"

S = list(S)

que = deque(S)

new_que = deque()

for i in range(len(S)):
    new_que.append(que.pop())

print("".join(new_que))
