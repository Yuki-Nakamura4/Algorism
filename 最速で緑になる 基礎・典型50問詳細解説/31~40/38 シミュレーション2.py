# 入力の受け取り
N, X = map(int, input().split())
S = input()

# 移動の記録
Move = []

# i=0~(N-1)
for i in range(N):
    # ・記録が空の場合
    if len(Move) == 0:
        # S[i]を記録
        Move.append(S[i])

    # ・記録が空でない場合
    else:
        # ・S[i]が「L」または「R」
        if S[i] == "L" or S[i] == "R":
            # S[i]を記録
            Move.append(S[i])
        # ・S[i]が「U」
        else:
            # ・S[i]が「U」かつ記録の末尾が「L」または「R」(「LU」「RU」になる場合)
            if Move[-1] == "L" or Move[-1] == "R":
                # 記録の末尾を消す
                Move.pop()
            # ・S[i]が「U」かつ記録の末尾が「U」
            else:
                # 「U」を記録
                Move.append(S[i])

# シミュレーション
for s in Move:
    # 「L」ならば2Xへ移動
    if s == "L":
        X *= 2
    # 「R」ならば(2X+1)へ移動
    elif s == "R":
        X = 2 * X + 1
    # 「U」ならばX//2へ移動
    else:
        X //= 2

# 答えの出力
print(X)
