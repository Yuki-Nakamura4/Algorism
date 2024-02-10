# 分からなかった

S = input()

def deleteABC(S):
    for i in range(len(S) - 2):
        if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
            S = S[:i] + S[i + 3 :]
            return S
    return S


while True:
    if "ABC" not in S:
        print(S)
        break
    else:
        S = deleteABC(S)
