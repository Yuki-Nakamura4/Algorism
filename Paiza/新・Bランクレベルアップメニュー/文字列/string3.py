# 自分の解答
# 正規表現を使えば楽
import re

S = input()

def leet(S):
    if re.search(r"p(a|4|@)(i|1|!)(z|2)(a|4|@)", S):
        return True

if "paiza" in S:
    print("paiza")
elif leet(S):
    print("leet") 
else:
    print("nothing")

# 模範解答
# 正規表現を使わずに実装している
# あらかじめleetになる文字列をリストにしておき、それぞれの文字列についてSの中に存在するかを確認している
S = input()
exist_leet = False
ok_char = ["p", "a4@", "i1!", "z2", "a4@"]

for i in range(len(S) - 4):
    is_leet = True 

    if S[i:i + 5] == "paiza":
        print("paiza")
        exit()

    for j in range(5):
        char_leet_ok = False
        for k in range(len(ok_char[j])):
            if S[i + j] == ok_char[j][k]:
                char_leet_ok = True
                break
        if not char_leet_ok:
            is_leet = False
            break

    if is_leet:
        exist_leet = True

if exist_leet:
    print("leet")
else:
    print("nothing")
