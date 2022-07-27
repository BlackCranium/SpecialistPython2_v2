suit_icons = {
    "Diamonds": '\u2662',
    "Hearts": '\u2661',
    "Spades": '\u2660',
    "Clubs": '\u2663'
}


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

cards = []
for suit in suits:
    for value in values:
        cards.append(Card(value, suit))

print(f"cards[{len(cards)}] {', '.join([card.to_str() for card in cards])}")
