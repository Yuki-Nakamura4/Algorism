Y, X, N = map(int, input().split())
D = [input() for _ in range(N)]

for direction in D:
    if direction == "N":
        Y -= 1
    elif direction == "E":
        X += 1
    elif direction == "S":
        Y += 1
    elif direction == "W":
        X -= 1
        
    print(Y, X)