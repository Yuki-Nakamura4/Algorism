# ひたすら2で割ってその余りを最下位桁から並べていく or 入植した数を2の累乗で割ってその商を2で割った余りを上から並べていく

def decimal_to_binary(decimal):
    binary = ""
    for _ in range(10):
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# 10進数を入力として受け取る
N = int(input())

# 2進数に変換
binary = decimal_to_binary(N)
print(binary)

# # 模範解答
# # 入力
# N = int(input())

# # 上の桁から順番に「2 進法に変換した値」を求める
# for x in [9,8,7,6,5,4,3,2,1,0]:
# 	wari = (2 ** x)
# 	print((N // wari) % 2, end='')

# # 最後に改行する
# print("")

