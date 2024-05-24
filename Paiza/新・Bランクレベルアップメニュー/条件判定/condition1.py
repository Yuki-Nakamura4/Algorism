y, x , h = map(int, input().split())
l = list(map(int, input().split()))
m = list(map(int, input().split()))
result = 0

if h <= l[0]:
    if max(y, x) <= l[1]:
        result = m[0]
    elif y + x <= l[2]:
        result = m[1]
    else:
        result = m[2]
else:
    if max(y,x) <= l[3]:
        result = m[3]
    elif y + x + h <= l[4]:
        result = m[4]
    else:
        result = y * x * h * m[5] 

print(result)