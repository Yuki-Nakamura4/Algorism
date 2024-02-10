# 入力の受け取り(文字列)
N = input()

# 答え 初期値は0
ans = 0

# bitnum=(000000),(000001),(000010),(000011),...,(111111)まで
for bitnum in range(1 << len(N)):
    # グループA,Bを用意
    A = []
    B = []

    # shift=0~(Nの桁数-1)まで
    for shift in range(len(N)):
        # bitnumのshift桁目が「0」か「1」か確認
        # 右にshift分シフト演算して「1」とアンド演算
        # 0ならば
        if bitnum >> shift & 1 == 0:
            # グループAへ追加
            A.append(N[shift])
        # 1ならば
        else:
            # グループBへ追加
            B.append(N[shift])

    # グループAまたはグループBが空なら
    if A == [] or B == []:
        # 次のbitnum
        continue

    # 大きい順に並び替え
    A.sort(reverse=True)
    B.sort(reverse=True)

    # A,Bを結合
    A_join = "".join(A)
    B_join = "".join(B)

    # 整数にして掛け算
    tmp_ans = int(A_join) * int(B_join)

    # ansよりtmp_ansが大きかったらansを更新
    ans = max(ans, tmp_ans)

# 答えの出力
print(ans)
