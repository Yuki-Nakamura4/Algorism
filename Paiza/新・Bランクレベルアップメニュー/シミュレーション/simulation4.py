# # 自分の解答
# in演算子でTがtのリストに存在するか確認しているが、これはリスト全体に対して線形探索を行うためO(n)となり非効率
# indexメソッドで特定の要素が存在するインデックスを取得しているが、これはリスト全体に対して線形探索を行うためO(n)となり非効率

# import math

# n = int(input())
# tArr = []
# yArr = []
# xArr=[]
# for i in range(n):
#     t, y, x = map(int, input().split())
#     tArr.append(t)
#     yArr.append(y)
#     xArr.append(x)
    
# for T in range(101):
#     if T in tArr:
#         index = tArr.index(T)
#         y, x = yArr[index], xArr[index]
#         print(y, x)
#     else:
#         for time in tArr:
#             if time > T:
#                 index = tArr.index(time)
#                 break
#         deltaY = (yArr[index] - yArr[index-1])/ (tArr[index] - tArr[index-1])
#         deltaX = (xArr[index] - xArr[index-1])/ (tArr[index] - tArr[index-1])
#         newY = math.ceil(yArr[index-1] + deltaY * (T - tArr[index-1]))
#         newX = math.ceil(xArr[index-1] + deltaX * (T - tArr[index-1]))
#         print(newY, newX)

# 模範解答
# now_indexという変数を利用することでリスト全体をスキャンする必要がなくなっている
n = int(input())
t = []
y = []
x = []

for _ in range(n):
    ti, yi, xi = map(int, input().split())
    t.append(ti)
    y.append(yi)
    x.append(xi)

now_index = 0

for i in range(101):
    if i == t[now_index]:
        print(y[now_index], x[now_index])
        now_index += 1
    else:
        y_i = y[now_index-1] + (i - t[now_index-1]) * (y[now_index] - y[now_index-1]) // (t[now_index] - t[now_index-1])
        x_i = x[now_index-1] + (i - t[now_index-1]) * (x[now_index] - x[now_index-1]) // (t[now_index] - t[now_index-1])
        print(y_i, x_i)