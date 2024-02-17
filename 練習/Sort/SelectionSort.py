def select_sort(data):
    """選択ソート：自分よりも小さな値と場所を入れ替えて，昇順に並べ替える"""
    # range(len(data)) => 0 ~ len(data)-1 まで
    for i in range(len(data)):
        Min = i  # 入れ替え対象をセット
        for j in range(i + 1, len(data)):
            # セットした値よりも小さな値があれば，その位置を最小値として記録
            if data[j] < data[Min]:
                Min = j
        # いまの位置と最小値を入れ替え ⇒ 結果，左から小さい順に並ぶ
        data[i], data[Min] = data[Min], data[i]

    return data  # 並べ替えを終えたデータを返す


if __name__ == "__main__":
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    sort = select_sort(DATA.copy())  # 後に比較するため，リストが変更されないようにcopyしたものを引数にする

    print(f"{DATA}  →  {sort}")
