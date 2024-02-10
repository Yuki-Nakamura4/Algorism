# 文字列Tが文字列Sにマッチするかどうか判定する関数
# マッチするときはTrueを、マッチしないときはFalseを返す
def is_match(T, S):
    # 文字列Sのi文字目から始まる部分が文字列Tとマッチするかどうか調べる
    for i in range(0, len(S) - len(T) + 1):
        # 文字列Sのi文字目から始まる部分が
        # 文字列Tとマッチしているかどうかを保持する変数
        ok = True

        # 文字列Tのj文字目と、文字列Sのi+j文字目を見比べる
        for j in range(0, len(T)):
            # 文字列Tのj文字目が文字列Sのi+j文字目と異なっていて
            # かつ、文字列Tのj文字目が"."でもない場合、
            # 文字列Sのi文字目から始まる部分は文字列Tとはマッチしない
            if S[i + j] != T[j] and T[j] != ".":
                ok = False

        # 文字列Sのi文字目から始まる部分が文字列Tとマッチしている場合
        # Trueを返す
        if ok:
            return True

    # 文字列Sのすべての部分について文字列Tとマッチしなかった場合、Falseを返す
    return False


S = input()

# 使える文字の一覧
C = "abcdefghijklmnopqrstuvwxyz."

# 文字列Sとマッチする文字列を格納する変数
M = []

# 長さ1の文字列をすべて調べ、SとマッチするものをMに入れる
for T in C:
    if is_match(T, S):
        M.append(T)

# 長さ2の文字列をすべて調べ、SとマッチするものをMに入れる
for c1 in C:
    for c2 in C:
        T = c1 + c2
        if is_match(T, S):
            M.append(T)

# 長さ3の文字列をすべて調べ、SとマッチするものをMに入れる
for c1 in C:
    for c2 in C:
        for c3 in C:
            T = c1 + c2 + c3
            if is_match(T, S):
                M.append(T)

print(len(M))
