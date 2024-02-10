# 全探索する解法

K = int(input())
A, B = map(int, input().split())

# Kの倍数がA以上B以下の範囲の中にあるかどうかを記録する変数
ok = False

# AからBまで順番に調べる。調べている数をxとする
for x in range(A, B + 1):
    # 調べている数xがKで割り切れるかどうか調べる
    if x % K == 0:
        ok = True

# Kで割り切れる数があれば、oKを出力する
if ok:
    print("OK")
else:
    print("NG")

######################
# 数学的な解法
K = int(input())

A, B = map(int, input().split())

# Kの倍数がA以上B以下の範囲の中にあるかどうかを記録する変数
ok = False

x = A // K
u = B // K

# x < u　ならばKの倍数がA以上B以下の範囲の中にある
if x < u:
    ok = True

if A % K == 0:
    ok = True

# Kで割り切れる数があればOKを出力する
if ok:
    print("OK")
else:
    print("NG")
