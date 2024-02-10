S = input()

ans = 0

for i in range(len(S)):
    if S[i] == ".":
        ans = i

print(S[ans:])


# 正規表現を使った解法
# import re

# S = input()
# print(re.search(r"[a-z]*$",S)[0])

# matchオブジェクトの配列の0番目の要素には、正規表現にマッチした文字列が入っている
