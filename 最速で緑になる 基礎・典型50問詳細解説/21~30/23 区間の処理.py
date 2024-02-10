# 入力の受け取り
N = int(input())

# 区間の格納リスト
section = []

# N回
for i in range(N):
    # 入力の受け取り
    t, l, r = map(int, input().split())
    # t=1の場合
    if t == 1:
        # 区間[l,r]を追加
        section.append([l, r])
    # t=2の場合
    elif t == 2:
        # 区間[l,r-0.1]を追加
        section.append([l, r - 0.1])
    # t=3の場合
    elif t == 3:
        # 区間[l+0.1,r]を追加
        section.append([l + 0.1, r])
    # t=4の場合
    elif t == 4:
        # 区間[l+0.1,r-0.1]を追加
        section.append([l + 0.1, r - 0.1])

# 答えの格納用変数
ans = 0

# i=0~(N-1)まで
for i in range(N):
    # j=(i+1)~(N-1)まで
    for j in range(i + 1, N):
        # 区間iの左端
        il = section[i][0]
        # 区間iの右端
        ir = section[i][1]
        # 区間jの左端
        jl = section[j][0]
        # 区間jの右端
        jr = section[j][1]

        # 「区間iと区間jの左端の最大値が、区間iと区間jの右端の最小値以下である」という条件
        #  区間iと区間jが重なっていることを意味する
        if max(il, jl) <= min(ir, jr):
            ans += 1

# 答えの出力
print(ans)
