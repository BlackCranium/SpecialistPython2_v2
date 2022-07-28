from deck_total import Card, Deck

deck = Deck()
deck.shuffle()
card1, = deck.draw(1)


def next_card():
    card, = deck.draw(1)
    print(str(card), end=" ")
    return card


print(str(card1))
while next_card() < card1:
    deck.shuffle()
