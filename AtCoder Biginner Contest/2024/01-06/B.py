N = int(input())

for x in range(N + 1):
    for y in range(N + 1):
        if x + y > N:
            continue
        for z in range(N + 1):
            if x + y + z > N:
                continue
            else:
                print(x, y, z)

# 模範解答
# for x in range(N+1):
#     for y in range(N+1):
#         for z in range(N+1):
#             if x + y + z <= N:
#                 print(x,y,z)
