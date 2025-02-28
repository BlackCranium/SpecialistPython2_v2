# Начнем с создания карты
suits = {
    "Diamonds": ['\u2662', "Бубны"],
    "Hearts": ['\u2661', "Червы"],
    "Spades": ['\u2660', "Пики"],
    "Clubs": ['\u2663', "Трефы"]
}

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        return f"{self.value}{suits[self.suit][0]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


# Создадим несколько карт
card1 = Card("10", "Hearts")
# card1 = Card("7", "Diamonds")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
