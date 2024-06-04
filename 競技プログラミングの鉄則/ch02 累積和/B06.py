N= int(input())
A= list(map(int, input().split()))
Q= int(input())
L, R = [None]*Q, [None]*Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())

cum_list = []
cum = 0
for i in range(N):
  cum  += A[i]
  cum_list.append(cum)

for q in range(Q):
    if L[q] == 1:
        hit_sum = cum_list[R[q]-1]
    else:
        hit_sum= cum_list[R[q]-1] - cum_list[L[q]-2]
    
    standard = (R[q] - L[q] + 1) / 2 # // 2とすると、[0, 1, 1, 0, 0]のようなときにdrawとなってしまい上手くいかない
    if  hit_sum > standard:
        print("win")
    elif hit_sum == standard:
        print("draw")
    else:
        print("lose")