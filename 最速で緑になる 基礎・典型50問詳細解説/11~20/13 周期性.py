N = int(input())
A = list(map(int, input().split()))
X = int(input())

# Aの合計
sum_A = sum(A)

Quotient = X // sum_A
Remainder = X % sum_A

step = 0

for i in range(len(A)):
    Remainder -= A[i]
    step += 1
    if Remainder < 0:
        break


# 何周したか
Round = Quotient * N

ans = Round + step

print(ans)


# # 入力の受け取り
# N=int(input())
# A=list(map(int, input().split()))
# X=int(input())

# # Aの合計
# Asum=sum(A)

# # 必要なAの数：X//(Aの合計)
# quo=X//Asum

# # 項数(k)：(Aの個数)×(Aの要素数)
# k=N*quo

# # 合計(Bsum)：(Aの個数)×(Aの合計)
# Bsum=Asum*quo

# # Xを超えるまでAの要素を順に足していく
# # i=0~(N-1)まで
# for i in range(N):
#     # 合計に+A[i]
#     Bsum+=A[i]
#     # 項数に+1
#     k+=1
#     # X<合計になったら
#     if X<Bsum:
#         # 答えを出力
#         print(k)
#         # 終了
#         exit()
