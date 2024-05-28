N, M = map(int, input().split())
win_list = []
lose_list= []
train_length = [1] * N

for i in range(M):
    x, y = map(int, input().split())
    win_list.append(x)
    lose_list.append(y)
    train_length[win_list[i] -1] += train_length[lose_list[i]-1]

winner_index = [i+1 for i, x in enumerate(train_length) if x == max(train_length)]

for winner in winner_index:
    print(winner)