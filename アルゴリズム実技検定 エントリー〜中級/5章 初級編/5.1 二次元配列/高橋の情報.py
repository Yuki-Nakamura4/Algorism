# 3*3の2次元配列となる予定の配列
C = []

for _ in range(0, 3):
    # Cの1行分を表す1次元配列
    row = list(map(int, input().split()))

    C.append(row)

# 矛盾していないかどうかを保持する変数
# 矛盾していたらFalse
ok = True

# Cの0列目と1列目の差を調べ、すべて同じ値でなければ矛盾
# まず左側で0行目と1行目について一致しているか判定。一致していなければその時点でFalseを返す
# 一致していた場合、右側の判定に移り、1行目と2行目について一致しているかの判定を行う。
# 一致していれば0行目=1行目=2行目となり、すべて一致で矛盾していない(ok = True)ということになる。
if C[0][0] - C[0][1] != C[1][0] - C[1][1] or C[1][0] - C[1][1] != C[2][0] - C[2][1]:
    ok = False

# Cの1列目と2列目の差を調べ、すべて同じ値でなければ矛盾
if C[0][1] - C[0][2] != C[1][1] - C[1][2] or C[1][1] - C[1][2] != C[2][1] - C[2][2]:
    ok = False

# Cの0行目と1行目の差を調べ、すべて同じ値でなければ矛盾
if C[0][0] - C[1][0] != C[0][1] - C[1][1] or C[0][1] - C[1][1] != C[0][2] - C[1][2]:
    ok = False

# Cの1行目と2行目の差を調べ、すべて同じ値でなければ矛盾
if C[1][0] - C[2][0] != C[1][1] - C[2][1] or C[1][1] - C[2][1] != C[1][2] - C[2][2]:
    ok = False

if ok:
    print("Yes")
else:
    print("No")
