N = int(input())

x, y = 0, 0

for i in range(N):
    X, Y = map(int, input().split())
    x += X
    y += Y

print("Talahashi" if x > y else "Aoki" if x < y else "Draw")
