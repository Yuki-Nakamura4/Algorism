# 自分の解答
X = int(input())
F_1, F_2 = map(int, input().split())
L, N = map(int, input().split())
S = list(map(int, input().split()))
S.insert(0,0)
S.append(L)

fuelAmount = 0

for i in range(1, N+2):
    partialDistance = S[i] - S[i-1]
    if partialDistance <= X:
        fuelAmount += F_1 * partialDistance
    else:
        fuelAmount += F_1 * X + F_2 * (partialDistance - X)

print(fuelAmount)

# `list(map(int, input().split()))`を `list[map(int, input().split())]`と記述していた(丸括弧を角括弧にしてしまっていた)ため、
# `TypeError: 'type' object is not subscriptable`` というエラーが発生した
# subscriptableは「インデックスで呼び出すことができる」という意味