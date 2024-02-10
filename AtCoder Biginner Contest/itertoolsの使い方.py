# 使いどころ：順列、組み合わせ、直積

import itertools

N, K = 4, 2

# 順列：permutations(range(始まり,終わり+1))
# p=(0,1,2,3),(0,1,3,2),(0,2,1,3),(0,2,3,1),...,(3,2,1,0)
print("[順列]")
for p in itertools.permutations(range(N)):
    print(p)

# 重複なしの組み合わせ：combinations(range(始まり,終わり+1),取る個数)
print("[重複なしの組み合わせ]")
# p=(0,1),(0,2),(0,3),(1,2)...,(2,3)
for p in itertools.combinations(range(N), K):
    print(p)

# 重複ありの組み合わせ：combinations_with_rep(range(始まり,終わり+1),取る個数)
print("[重複ありの組み合わせ]")

# p=(0,0),(0,1),(0,2),(0,3),(1,1)...,(3,3)
for p in itertools.combinations_with_replacement(range(N), K):
    print(p)

# 直積：product(range(始まり,終わり+1),range(始まり,終わり+1)):
print("[直積]")
# p=(0,0),(0,1),(0,2),(0,3),(1,0)...,(3,3)
for p in itertools.product(range(N), range(N)):
    print(p)
