N = int(input())

ans = 0

# Aに1からN-1までの値を代入して、Aを固定する
for A in range(1, N):
    # Aを固定したとき、BはNを超えない範囲で取りうる値すべてを試す
    for B in range(1, N):
        # Aを固定したときにN>=A*BとなるBの個数を数える
        b_count = (N - 1) // A
        ans += b_count

print(ans)
