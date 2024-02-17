def insert_sort(data):
    """挿入ソート：少しずつソート済み箇所を広げ，昇順に並べ替える"""
    # いちばん左端の数字を操作済みにし、その右隣からスタート
    for i in range(1, len(data)):
        temporary = data[i]  # 挿入データを一時的に記録
        j = i - 1  # 挿入データの左隣のインデックス
        # 左にある操作済みのデータが右にある挿入データより大きければ
        while (j >= 0) and (data[j] > temporary):
            # 操作済みのデータの位置を右側に変更する
            data[j + 1] = data[j]
            # 左隣の操作済みデータに移り比較を繰り返す
            j -= 1
        # 挿入データよりも小さい操作済みデータに出会ったら、その右隣に挿入データを挿入
        data[j + 1] = temporary

    return data


if __name__ == "__main__":
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

    sorted_data = insert_sort(DATA.copy())

    print(f"{DATA} → {sorted_data}")
