N = int(input())

A = list(map(int, input().split()))

increase = 0
necessary_people = 0

for i in range(N):
    increase += A[i]
    if increase < 0:
        necessary_people = max(necessary_people, -increase)

print(increase + necessary_people)
