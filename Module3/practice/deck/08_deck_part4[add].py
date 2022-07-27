import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icons = {"Diamonds": '\u2662', "Hearts": '\u2661', "Spades": '\u2660', "Clubs": '\u2663'}
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        # ♥ > ♦ > ♣ > ♠
        suit_values = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}
        values_num = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                      'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        if self.value == other_card.value:
            return suit_values[self.suit] > suit_values[other_card.suit]
        return values_num[self.value] > values_num[other_card.value]

    def less(self, other_card):
        # ♥ > ♦ > ♣ > ♠
        suit_values = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}
        values_num = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                      'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        if self.value == other_card.value:
            return suit_values[self.suit] < suit_values[other_card.suit]
        return values_num[self.value] < values_num[other_card.value]


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        return f"deck[{len(self.cards)}] {', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        res = self.cards[:x]
        self.cards = self.cards[x:]
        return res

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):
        self.cards = self.cards[num_card:] + self.cards[:num_card]


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(10)
print(deck.show())
