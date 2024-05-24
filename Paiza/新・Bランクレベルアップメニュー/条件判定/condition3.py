# 自分の解答
# 一部上手く動かなかった
# import math

# N = int(input())
# S = input()
# V = []
# for i in range(N):
#     v = input()
#     V.append(v)

# for word in V:
#     if word == S:
#         print("banned")
#     else:
#         forwardWord = word[:math.ceil(len(S)/2)]
#         backWord =  word[math.ceil(len(S)/2):]
#         if forwardWord == S[:math.ceil(len(S)/2)]:
#             print("x" * math.ceil(len(S)/2) + word[(len(S)//2 + 1):])
#         elif backWord ==  S[math.ceil(len(S)/2):]:
#             print(word[:math.ceil(len(S)/2)-1] + "x" * math.floor(len(S)/2))
#         else:
#             print(word)

# 模範解答
N = int(input())
S = input()
V = [input() for _ in range(N)]

for word in V:
    if len(word) == len(S):
        if word == S:
            print("banned")
        else:
            half_len = (len(S) + 1) // 2 # こうすれば奇数の場合も同じように半分の長さを取得できる
            if word[:half_len] == S[:half_len]:
                print('x' * half_len + word[half_len:])
            elif word[len(S) // 2:] == S[len(S) // 2:]:
                print(word[:len(S) // 2] + 'x' * half_len)
            else:
                print(word)
    else:
        print(word)