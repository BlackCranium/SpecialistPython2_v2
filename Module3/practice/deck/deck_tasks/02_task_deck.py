from deck_total import Card, Deck

deck = Deck()

deck.shuffle()

hand = deck.draw(15)

suits = {Card.CLUBS: len([card for card in hand if card.suit == Card.CLUBS]),
         Card.HEARTS: len([card for card in hand if card.suit == Card.HEARTS]),
         Card.DIAMONDS: len([card for card in hand if card.suit == Card.DIAMONDS]),
         Card.SPADES: len([card for card in hand if card.suit == Card.SPADES])}

print(hand)
# print(suits)
more_suits = dict(filter(lambda item: item[1] == max(suits.values()), suits.items()))
# print(more_suits)
print("Много:", ", ".join(more_suits.keys()))
