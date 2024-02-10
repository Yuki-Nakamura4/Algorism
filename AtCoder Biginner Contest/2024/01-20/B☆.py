# 正規表現を用いる
import re

S = input()

print("Yes" if re.fullmatch("A*B*C*", S) else "No")
# "A*B*C*"　<= 0回以上のAの後に0回以上のBが続き、その後に0回以上のCが続く任意の文字列


# 正規表現を使わない解法

S = input()
ans = False
for i in range(len(S)+1):
    for j in range(len(S)-i+1):
        t = "A" * i + "B" * j + "C" * (len(S)-i-j)
        ans |= t == S # tとSが一致していたらansをTrueにする
print("Yes" if ans else "No")
