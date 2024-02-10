# 数学的な解法

import math

N = int(input())

# N番目のゾロ目数の桁数
# math.ceil => xの小数点以下を切り上げた数を得る
x = math.ceil(N / 9)

# N番目のゾロ目数の数字
y = N % 9

if y == 0:
    y = 9

# 答えの文字列
ans = ""

# 答えはyがx桁並んだものになる
for _ in range(0, x):
    ans += str(y)

print(ans)


# 全探索による解法

N = int(input())

# 今までに出てきたゾロ目の数
z = 0

# 1から555555までの整数をすべて調べる。調べている数をiとする。
for i in range(1, 555555 + 1):
    # iがゾロ目かどうかを調べるために、iを文字列にしたsiを作る
    si = str(i)

    # iがゾロ目数だったかどうかを保持する変数
    ok = True

    # siのすべての文字がsiの0文字目と同じかどうかを調べる
    # siの0文字目と異なる文字が含まれていたら、iはゾロ目数ではない
    for s in si:
        if s != si[0]:
            ok = False

    # iがゾロ目数のとき、出てきたゾロ目数の数を1増やす
    if ok:
        z += 1

    # iがゾロ目数で、N番目に出てきたゾロ目数ならば、答えとして保存する
    if ok and z == N:
        ans = i

print(ans)
