# 模範解答
# 斜め(D==1とD==4)が難しい
# 斜め方向のナンバリングでは、各斜め列の最初の要素に注目してから斜めに移動していくイメージを持つとナンバリングのイメージがしやすい
H, W, D = map(int, input().split())
count = 1
ans = [[0] * W for _ in range(H)] # 答えとなる配列を初期化

if D == 1:
    ans[0][0] = 1
    count += 1
    for i in range(1, H): # 対角線の上(左)半分。左端の列からスタートできるものは行数分存在する
        for j in range(min(i+1, W)): # 斜めに何マス置けるか。基本的には1ずつ増えていくが、最大列数で制限される
            ans[i - j][j] = count # 1番目はiから上に1行動いた1列目、2番目はiから上に2行動いた2列目
            count += 1
    for i in range(1, W): # 対角線の下(右)半分。いちばん下の行からスタートできるものは列数分存在する
        for j in range(min(H, W - i)): # 斜めに何マス置けるか。基本的にはスタート位置(iの列)から横幅終端までだが、最大行数で制限される
            ans[H - 1 - j][i + j] = count
            count += 1
elif D == 2:
    for i in range(H):
        for j in range(W):
            ans[i][j] = count
            count += 1
elif D == 3:
    for i in range(W):
        for j in range(H):
            ans[j][i] = count
            count += 1
elif D == 4:
    ans[0][0] = 1
    count += 1
    for i in range(1, W):
        for j in range(min(i+1, H)):
            ans[j][i - j] = count
            count += 1
    for i in range(1, H):
        for j in range(min(H - i, W)):
            ans[i + j][W - 1 - j] = count
            count += 1

for row in ans:
    print(" ".join(map(str, row)))