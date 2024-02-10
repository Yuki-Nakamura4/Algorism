N = int(input())

num = []

lst = [1, 11, 111, 1111, 11111]

for i in range(0, 5):
    for j in range(0, 5):
        for k in range(0, 5):
            num.append(lst[i] + lst[j] + lst[k])

ans = sorted(set(num))

print(ans[N - 1])
