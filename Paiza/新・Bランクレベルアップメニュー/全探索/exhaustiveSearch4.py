import itertools

s = []
for _ in range(3):
    s.extend(map(int, input().split()))

# 中央か角か辺か
b = [[] for _ in range(9)]
for i in range(9):
    if i == 4:
        b[i] = list(map(int, input().split()))
    elif i % 2 == 0:
        b[i] = list(map(int, input().split()))
    else:
        b[i] = list(map(int, input().split()))

ans = sum(s) # すべてのマスを開けたときの得点
panels = list(range(9)) # パネルの番号
add = 0 # 追加の得点を計算し、その中で最大の値を保持するための変数

# すべてのパネルの並び方について、得点を計算する
for perm in itertools.permutations(panels):
    opened_panel = [False] * 9
    tmp = 0 # パネルの並び方1つについての得点
    for i in range(9):
        line = 0 # パネルiを開けたことによってできたラインの数
        if perm[i] == 0:
            line += (opened_panel[1] and opened_panel[2]) # 両方trueなら1を足す
            line += (opened_panel[3] and opened_panel[6])
            line += (opened_panel[4] and opened_panel[8])
        elif perm[i] == 1:
            line += (opened_panel[0] and opened_panel[2])
            line += (opened_panel[4] and opened_panel[7])
        elif perm[i] == 2:
            line += (opened_panel[0] and opened_panel[1])
            line += (opened_panel[5] and opened_panel[8])
            line += (opened_panel[4] and opened_panel[6])
        elif perm[i] == 3:
            line += (opened_panel[0] and opened_panel[6])
            line += (opened_panel[4] and opened_panel[5])
        elif perm[i] == 4:
            line += (opened_panel[0] and opened_panel[8])
            line += (opened_panel[2] and opened_panel[6])
            line += (opened_panel[1] and opened_panel[7])
            line += (opened_panel[3] and opened_panel[5])
        elif perm[i] == 5:
            line += (opened_panel[2] and opened_panel[8])
            line += (opened_panel[3] and opened_panel[4])
        elif perm[i] == 6:
            line += (opened_panel[0] and opened_panel[3])
            line += (opened_panel[2] and opened_panel[4])
            line += (opened_panel[7] and opened_panel[8])
        elif perm[i] == 7:
            line += (opened_panel[1] and opened_panel[4])
            line += (opened_panel[6] and opened_panel[8])
        elif perm[i] == 8:
            line += (opened_panel[2] and opened_panel[5])
            line += (opened_panel[6] and opened_panel[7])
            line += (opened_panel[0] and opened_panel[4])
        
        if line > 0:
            tmp += b[perm[i]][line - 1] # 得点を加算
        opened_panel[perm[i]] = True # パネルiを開けたことを記録

    add = max(add, tmp)

print(ans + add)