N, Q = map(int, input().split())
A= list(map(int, input().split()))
L, R = [], []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
cum_list = []
cum = 0
for i in range(N):
  cum  += A[i]
  cum_list.append(cum)
for i in range(Q):
    if L[i] == 1:
        print(cum_list[R[i]-1])
    else:
        print(cum_list[R[i]-1] - cum_list[L[i]-2])

# 模範解答
N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [ None ] * Q # あらかじめ配列のサイズを決めておくとメモリの再割り当てが発生しないためメモリ効率が良い
R = [ None ] * Q
for j in range(Q):
	L[j], R[j] = map(int, input().split())
 
S = [ None ] * (N + 1)
S[0] = 0
for i in range(N):
	S[i + 1] = S[i] + A[i]
 
for j in range(Q):
	print(S[R[j]] - S[L[j] - 1])