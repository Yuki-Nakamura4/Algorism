N = int(input())
C = list(map(int, input().split()))
Q = int(input())

# 合計販売枚数を記録する変数
sell = 0

# 全種類販売で販売した1種類あたりの枚数
z = 0

# セット販売で販売した1種類あたりの枚数
s = 0

# セット販売対象のCの最小値を記録する変数
# 最小値を求めるときは、いちばん最初に適当に大きい数を代入しておく
min_s_C = 1000000000

# セット販売対象でないCの最小値を記録する変数
min_z_C = 1000000000

for i in range(0, N):
    if i % 2 == 0:
        min_s_C = min(C[i], min_s_C)
    else:
        min_z_C = min(C[i], min_z_C)

for _ in range(0, Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # 単品販売の場合
        x = query[1] - 1
        a = query[2]

        # カードxの残っている枚数を計算する
        if x % 2 == 0:
            # セット販売対象のカードの場合
            card_x = C[x] - z - s
        else:
            # セット販売対象のカードではない場合
            card_x = C[x] - z

        # カードxがa枚以上残っていればa枚売る
        if card_x >= a:
            C[x] -= a
            sell += a

            if x % 2 == 0:
                min_s_C = min(C[x], min_s_C)
            else:
                min_z_C = min(C[x], min_z_C)

    elif query[0] == 2:
        # セット販売の場合
        a = query[1]

        # i%2==0となるC[i]の最小値について、そのカードがa枚以上あるかどうか調べる
        # a枚以上の場合、a枚得る
        if min_s_C - s - z >= a:
            s += a

    elif query[0] == 3:
        # 全種類販売の場合
        a = query[1]

        # Cの最小値について、そのカードがa枚以上あるかどうか調べる
        # a枚以上の場合、a枚ずつ売る
        if min(min_s_C - s - z, min_z_C - z) >= a:
            z += a

# #セット販売した枚数を合算する
# for i in range(0, N):
#     if i % 2 == 0:
#         sell += s

sell += s * ((N + 1) // 2)

# 全種類販売した枚数を合算する
sell += z * N

print(sell)
