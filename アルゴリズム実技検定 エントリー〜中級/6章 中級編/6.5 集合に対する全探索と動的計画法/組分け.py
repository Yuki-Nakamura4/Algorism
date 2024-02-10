N = int(input())

# A[i][j]:iとjが同じグループに属するときの幸福度の二次元配列
A = []

# 組み合わせを受け取るのでN-1行分だけでOK
for i in range(N - 1):
    # A[i]はA[i][i+1]からスタートするため、0からiまでの(i+1)個はダミーで埋める
    lst = list(map(int, input().split()))
    A.append([0] * (i + 1) + lst)

# 集合としてあり得るものの個数。2**Nでも同じ。
# つまり、個数を二進数で表現している
# <<はビットシフト演算子。つまり、1をNビット左にシフトする。
# たとえばN=2のとき、表現され得る個数は2**2=4なので、1 << 2で100(2進数)となる
ALL = 1 << N

# happy[n]:nで表現される集合をグループにしたときの幸福度
happy = [0] * ALL


# nで表現される集合に要素iが含まれるかどうかを判定してTrue/Falseを返す関数
def has_bit(n, i):
    return n & (1 << i) > 0


# happyの値を前もって計算する
for n in range(ALL):
    for i in range(N):
        for j in range(i + 1, N):
            if has_bit(n, i) and has_bit(n, j):
                happy[n] += A[i][j]

# 答えの値。非常に小さい値で初期化して、maxで更新していく
ans = -(10**100)

for n1 in range(ALL):
    for n2 in range(ALL):
        # n1とn2が重複している場合はスキップ
        if n1 & n2 > 0:
            continue
        # n3を補集合として計算し答えを更新する
        n3 = ALL - 1 - (n1 | n2)
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])

print(ans)
