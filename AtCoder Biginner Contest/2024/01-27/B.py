from collections import defaultdict

S = input()

count = defaultdict(int)  # 0で初期化された辞書

for i in S:
    count[i] += 1

ans = max(count.values())