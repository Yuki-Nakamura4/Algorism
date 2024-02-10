N = int(input())
M = int(input())
X = list(map(int, input().split()))

tour_length = 0
count_path = []

for i in range(M):
    tour_length += min(X[i+1]-X[i], N-X[i+1]+X[i])




