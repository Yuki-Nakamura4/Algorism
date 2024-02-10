N, M = map(int, input().split())

S = [int(x) for x in list(str(input()))]
S.insert(0, 0)

logo = [0] * (N+1)
logo[0]= 0

m = M

for i in range(N+1):
    if S[i] == 0:
        logo[i] = 0
        m = M
    elif S[i] == 1:
        if m > 0:
            m -= 1
            logo[i] = logo[i-1]
        else:
            logo[i] = logo[i-1] + 1
    elif S[i] == 2:
        logo[i] = logo[i-1] + 1

ans = max(logo)

print(ans)