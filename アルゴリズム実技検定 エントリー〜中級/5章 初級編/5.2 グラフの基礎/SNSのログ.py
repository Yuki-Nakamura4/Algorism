N, Q = map(int, input().split())

# FalseのN*Nの2次元配列を作る
graph = []
for i in range(0, N):
    # 長さNのFalseの1次元配列を作る
    row = []
    for j in range(0, N):
        row.append(False)

    # 長さNのFalseの1次元配列をgraphに追加する
    graph.append(row)

# Q個の操作を受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))

    # 頂点番号は-1する
    a = query[1] - 1

    # 「フォロー」の操作の場合
    if query[0] == 1:
        # 頂点番号は-1する
        b = query[2] - 1

        # aからbへと辺を張る
        graph[a][b] = True

    # 「フォロー全返し」の操作の場合
    if query[0] == 2:
        # 全ての頂点を順番に見る。見ている頂点をvとする
        for v in range(0, N):
            # 頂点vから頂点aへと辺があるとき
            if graph[v][a]:
                graph[a][v] = True

    # 「フォローフォロー」の操作の場合
    if quwry[0] == 3:
        # 頂点aから辺を張る予定の頂点のリスト
        to_follow = []

        # すべての頂点を順番に見る。見ている頂点をvとする。
        for v in range(0, N):
            # 頂点aから頂点vに辺があるとき
            if graph[a][v]:
                # さらにすべての頂点を順番に見る。見ている頂点をwとする。
                for w in range(0, N):
                    # 頂点vから頂点wへと辺があり、かつwがaではないとき
                    if graph[v][w] and w != a:
                        # あとで頂点aから辺を張るために記録しておく
                        to_follow.append[a][w]

            # 頂点aから辺を張る
            for w in to_follow:
                graph[a][w] = True

# 隣接行列をすべて出力する
for i in range(0, N):
    for j in range(o, N):
        # iからjへと辺がある場合はYを、辺がない場合はNを出力する。改行はしない。
        if graph[i][j]:
            print("Y", end="")
        else:
            print("N", end="")

    # N文字出力するごとに改行する
    print()
