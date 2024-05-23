# # 自分の解答
# def shuffle(deck):
#     newDeck = []
#     upperDeck = deck[:26] # 上半分のデッキ
#     lowerDeck = deck[26:] # 下半分のデッキ
#     for i in range(1,27):
#         newDeck.insert(0, lowerDeck[-i])
#         newDeck.insert(0, upperDeck[-i])
#     return newDeck

# K = int(input())
# suits = ["S_", "H_", "D_", "C_"]
# cards = []

# # カードの文字列をを生成
# for suit in suits:
#     for num in range(1, 14):
#         card = suit + str(num)
#         cards.append(card)

# # K回シャッフルを行う
# for i in range(K):
#     cards = shuffle(cards)

# for card in cards:
#     print(card)


# リファクタリング後
# insertの使用は非効率なのでappendに変更し、代わりに追加順を逆にした
# shuffleの回数を表すインデックスをiではなく_に変更した
def shuffle(deck):
    newDeck = []
    upperDeck = deck[:26]  # 上半分のデッキ
    lowerDeck = deck[26:]  # 下半分のデッキ
    for i in range(26):
		# 配列の末尾に追加。元が下半分の一番下→上半分の一番下→...という順で先頭に追加だったので
		# 逆算して上半分の一番上→下半分の一番上の順で末尾に追加するようにすれば同じになる
        newDeck.append(upperDeck[i]) 
        newDeck.append(lowerDeck[i])
    return newDeck

K = int(input())
suits = ["S_", "H_", "D_", "C_"]
cards = []

# カードの文字列を生成
for suit in suits:
    for num in range(1, 14):
        card = suit + str(num)
        cards.append(card)

# K回シャッフルを行う
for _ in range(K):  # i を _ に変更
    cards = shuffle(cards)

for card in cards:
    print(card)