# 自分の解答
# 文字列はすべて文字(当たり前)なので type(S[i]) == int などするとすべてfalseになってしまう
# isdigit() で数値かどうか判定できる

# S = input()

# for i in range(len(S)):
#     if S[i].isdigit(): # isdigitを使用
#         temp_index = []
#         for j in range (i, len(S)):
#             if S[j].isdigit():
#                 temp_index.append(j)
#         for k in temp_index:
#             print(S[i:k+1])

#　模範解答
# 自分の解答の方が計算量としては効率的
# 模範解答ではすべてのiとjの組みわせについてスキャンし、それらが両方数値である場合に出力している
# 自分の解答ではiが数値である場合のみその後の文字をスキャンしている
# 可読性は模範解答の方が高い
S = input()

for i in range(len(S)):
    for j in range(i, len(S)):
        if S[i].isdigit() and S[j].isdigit():
            print(S[i:j + 1])