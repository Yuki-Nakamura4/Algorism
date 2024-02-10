import numpy as np

N = int(input())

np.base_repr(N, 5)

# 5進数で表記したときの各桁を2倍して、文字列に変換して、結合する
print("".join(map(lambda x: str(int(x) * 2), np.base_repr(N - 1, 5))))

# def decimal_to_base5(decimal_number):
#     if decimal_number == 0:
#         return '0'
#     base5_digits = []
#     while decimal_number > 0:
#         remainder = decimal_number % 5
#         base5_digits.append(str(remainder))
#         decimal_number //= 5

#     return ''.join(reversed(base5_digits))

# decimal_number = int(input())
