K, G, M = map(int, input().split())

m = 0
g = 0

i = 0
while i < K:
    if g == G:
        g = 0
        i += 1
    elif m == 0:
        m = M
        i += 1
    else:
        if G-g >= m:
            g += m
            m = 0
            i += 1
        else:
            m -= G-g
            g = G
            i += 1

print(g, m)

