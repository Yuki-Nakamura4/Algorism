N, S, K = map(int, input().split())

amount = 0

for i in range(N):
    p, q = map(int, input().split())
    amount += p * q

if amount >= S:
    print(amount)
else:
    print(amount + K)
