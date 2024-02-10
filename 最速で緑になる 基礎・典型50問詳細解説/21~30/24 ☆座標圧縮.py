# 入力の受け取り
H, W, N = map(int, input().split())

# カードの[行番号,列番号]を受け取るリスト
cards = []
# 行番号だけ受け取るリスト
rows = []
# 列番号だけ受け取るリスト
columns = []

# N回
for i in range(N):
    # 入力の受け取り
    A, B = map(int, input().split())
    # カードの[行番号,列番号]を受け取り
    cards.append([A, B])
    # 行番号を受け取り
    rows.append(A)
    # 列番号を受け取り
    columns.append(B)

# 重複の削除(setにする)
rows = set(rows)
# リストに直す(setはソートできない)
rows = list(rows)
# ソートする
rows.sort()

# 変換先を記録する連想配列
rowsConvert = dict()

# 重複削除後の行の個数分
for i in range(len(rows)):
    # もとの行番号→インデックス番号+1と変換できるように記録(小さい方から何番目にあるか？)
    rowsConvert[rows[i]] = i + 1

# 列も同じことをする
columns = set(columns)
columns = list(columns)
columns.sort()

columnsConvert = dict()

for i in range(len(columns)):
    columnsConvert[columns[i]] = i + 1

# それぞれのカードについて行、列番号を変換して出力
for rows, columns in cards:
    # 行番号の変換
    ansRows = rowsConvert[rows]
    # 列番号の変換
    ansColumns = columnsConvert[columns]
    # 答えを出力する
    print(ansRows, ansColumns)
