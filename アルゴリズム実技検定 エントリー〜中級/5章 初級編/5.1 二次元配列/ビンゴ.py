# ビンゴカードを表す2次元配列となる予定の配列
A = []

for _ in range(3):
    # ビンゴカードの1行を受け取る
    row = list(map(int, input().split()))

    # 受け取った1行分の配列をAの末尾に追加する
    # Aは1次元配列を要素とする配列であるため、Aは2次元配列である
    A.append(row)

# ビンゴカードに書かれている数字に印がついているかどうかを記録する2次元配列
# 大きさは3*3
# i行目j列目の数字に印がついている、M[i][j]=Trueとなるようにする
# 最初は印がついている数字はないため、すべてFalseにしておく
M = []

for i in range(0, 3):
    row = []
    for j in range(0, 3):
        row.append(False)

    M.append(row)

N = int(input())

# 選ばれた数字がビンゴカードに書かれているかを確認する
for _ in range(0, N):
    # 選ばれた数字
    b = int(input())

    # bがビンゴカードに書かれている確認する
    for i in range(0, 3):
        for j in range(0, 3):
            if A[i][j] == b:
                # 　もしビンゴカードのi行目j列目に数字bがあれば
                # M[i][j]=Trueとして印をつける
                M[i][j] = True

# 　ビンゴを達成しているかどうかを調べる

# ビンゴを達成しているかどうかを記録する変数
bingo = False

for i in range(0, 3):
    # i行目の3つの印がついているか調べる
    # 印がついていたらビンゴ達成となる
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0, 3):
    # i列目の3つに印がついているか調べる
    # 印が付いていたらビンゴ達成となる
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

# 左上から右下にかけて、斜めに3つ印がついているか調べる
if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

# 右上から左下にかけて、斜めに3つ印がついているか調べる
if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

# 　ビンゴ達成していたらYesを出力
if bingo:
    print("Yes")
else:
    print("No")
