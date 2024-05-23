# 模範解答
S = input()
for i in range(len(S)):
    # countの内部で文字列を何周もしているが、問題ない
    if S.count(S[i]) == i:
        print(i + 1)

# 自分の解答
S = input()

for i in range(1, len(S)):
    if S[0] != S[1] and S[0] != S[2]:
        print(1)
        exit()
    elif S[i] != S[i - 1]:
        print(i + 1)
        exit()
