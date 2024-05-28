X, Y, N = map(int, input().split())

count = 0
for i in range(N):
    count += i *2 + 1
    if count > N:
        break
    else:
        X += i * 2 + 1

    count += i *2 + 1
    if count > N:
        break
    else:
        Y += i *2 + 1

    count += (i + 1) * 2
    if count > N:
        break
    else:
        X -= (i + 1) * 2

    count += (i + 1) * 2
    if count > N:
        break
    else:
        Y -= (i + 1) * 2

print(X, Y)