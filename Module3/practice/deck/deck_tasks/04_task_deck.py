from deck_total import Deck


Deck.values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck1 = Deck()
deck2 = Deck()
# print(deck1)
# print(deck2)
deck1.shuffle()
deck2.shuffle()
score = [0, 0]

while len(deck1.cards) > 0:
    card1, = deck1.draw(1)
    card2, = deck2.draw(1)
    if card1 > card2:
        score[0] += 1
    elif card1 < card2:
        score[1] += 1
    # print(f"{card1} {card2} {score[0]}:{score[1]}")
print(f"Итоговый счет: {score[0]}:{score[1]}")
