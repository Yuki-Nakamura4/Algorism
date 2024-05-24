# # 自分の解答
# # 冗長
# # 辞書のソートでO(NlogN)がかかってしまうため、全体の計算量はO(NlogN)
# N = int(input())
# Tests =[]
# Judges = []
# for i in range(N):
#     T, J = input().split()
#     Tests.append(T)
#     Judges.append(J)

# success = {}
# failure={}

# testNames = set(Tests)
# for name in testNames:
#     success[name] = 0
#     failure[name] = 0

# for i in range(N):
#     if Judges[i] == "ok":
#         if failure[Tests[i]] < 2 :
#             success[Tests[i]] += 1
#     else:
#         failure[Tests[i]] += 1

# sorted_success = sorted(success.keys())

# for i in sorted_success:
#     if success[i] >= 2:
#         result = i[1]
#         print(result)
#         exit()

# print("E")


# 模範解答
# 計算量はO(N)
# 被験者のレベルを表すtester_levelという変数で現時点のレベルを管理している
# 成功・失敗は配列で管理し、A~Dをそれぞれ0~3のインデックスに割り当てている
def tests(level, result):
    global tester_level
    if result == "ok":
        ok[level] += 1
    else:
        ng[level] += 1

    if ok[level] == 2 and ng[level] < 2:
        tester_level = min(tester_level, level)


tester_level = 4
ok = [0] * 4
ng = [0] * 4

test_name = ["TA", "TB", "TC", "TD"]
level_name = ["A", "B", "C", "D", "E"]

n = int(input())
for _ in range(n):
    test, result = input().split()
    for j in range(4):
        if test == test_name[j]:
            tests(j, result)

print(level_name[tester_level])
