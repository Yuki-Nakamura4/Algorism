# エラトステネスの篩
def Eratosthenes(N):
    # 素数であるかの判定リスト
    IsPrime = [True] * (N + 1)

    # i=2,3,4,...
    i = 2
    # i≤√Nまで⇔i^2≤Nまで
    while i**2 <= N:
        # iが素数でなければ
        if IsPrime[i] == False:
            # 次のiへ
            i += 1
            continue

        # k=2,3,4,...
        k = 2
        while i * k <= N:
            # iの倍数は素数でない
            IsPrime[i * k] = False
            # 次のkへ
            k += 1

        # 次のiへ
        i += 1

    # 素数リスト
    PList = []

    # i=2~N
    for i in range(2, N + 1):
        # iが素数ならば
        if IsPrime[i] == True:
            # リストへ入れる
            PList.append(i)

    # リストを返す
    return PList


# 入力の受け取り
N = int(input())
# 10^6以下の素数リストを作成
P = Eratosthenes(10**6)

# 答え
ans = 0

# 素数リストの長さ
lenP = len(P)

# 最後の素数の番号(0インデックス)
k = lenP - 1

# i=0~(lenP-1)
for i in range(lenP):
    # p=i番目の素数(0インデックス)
    # q=k番目の素数(0インデックス)
    # p*q^3≤Nとなるまでkを減らしていく
    while i < k and N < P[i] * P[k] ** 3:
        k -= 1

    # k≤iとなったら
    if k <= i:
        # 答えの出力
        print(ans)
        # 途中終了
        exit()

    # i+1,i+2,...,k番目の素数までqとして使用できる
    # ⇔(k-i)個
    ans += k - i
