N = int(input())

Used = [False] * (2 * N + 2)

# 最初は1を出力
print(1)

# 1を使ったのでTrue
Used[1] = True

# N回繰り返す
for i in range(N + 1):
    # 青木くんの番
    x = int(input())
    # xを使用済みにする
    Used[x] = True
    # x = 「0」の場合
    if x == 0:
        # 終了
        exit()

    for k in range(1, 2 * N + 1):
        if Used[k] == False:
            # kを出力
            print(k)
            # kを使用済みにする
            Used[k] = True
            # 終了
            break
