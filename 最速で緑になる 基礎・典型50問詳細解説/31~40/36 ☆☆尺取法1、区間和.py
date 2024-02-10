# 尺取法は、左右のインデックス番号を条件に合わせて動かしながら区間の長さ等を計算するアルゴリズム

S = input()
K = int(input())

S = "?" + S

N = len(S)

# 「.」の累積個数
Count = [0] * N

# その文字までの「.」の累積個数を計算
for i in range(1, N):
    # S[i]=「X」ならば
    if S[i] == "X":
        # 一つ左と同じ
        Count[i] = Count[i - 1]
    # そうでないなら(S[i]=「.」)
    else:
        # 一つ左+1
        Count[i] = Count[i - 1] + 1

# 答え
ans = 0

# 右
r = 1

# l=1~(N-1)
for l in range(1, N):
    # r<Nの間
    while r < N:
        # [左,右]にある「.」の数=Count[r]-Count[l-1]
        Period = Count[r] - Count[l - 1]

        # [左,右]にある「.」の数≤Kならば
        # ⇔[左,右]にある「.」を全て「X」に変えられるなら
        if Period <= K:
            # 右を移動
            r += 1
        # そうでないなら([左,右]にある「.」を全て「X」に変えられないなら)
        else:
            # whileを抜ける
            break

    # [左,右-1]の長さを計算し、今までの答えより大きければ更新
    ans = max(ans, r - l)

# 答えの出力
print(ans)
