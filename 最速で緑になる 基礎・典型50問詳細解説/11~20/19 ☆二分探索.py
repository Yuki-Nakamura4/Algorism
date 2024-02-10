N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()


def binary_search(x):
    l = 0
    r = N - 1

    while 1 < r - l:
        c = (l + r) // 2

        if A[c] > x:
            r = c
        elif A[c] < x:
            l = c
        else:
            return c

    return r


for i in range(Q):
    x = int(input())

    if x <= A[0]:
        print(N)
    elif A[N - 1] < x:
        print(0)
    else:
        print(N - binary_search(x))
