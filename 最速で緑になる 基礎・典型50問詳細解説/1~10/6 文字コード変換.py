# アルファベットをインポート
import string

# アルファベットを格納
alphabet = string.ascii_lowercase

P = list(map(int, input().split()))

ans =[]

for i in range(26):
    ans.append(alphabet[P[i]-1])

print("".join(ans))