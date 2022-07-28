import random


class Card:

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icons = {"Diamonds": '\u2662', "Hearts": '\u2661', "Spades": '\u2660', "Clubs": '\u2663'}
        return f"{self.value}{suit_icons[self.suit]}"

    def __str__(self):
        return self.to_str()

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __cost(self):
        suit_cost = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}
        values_cost = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                       'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return values_cost[self.value] * 4 + suit_cost[self.suit]

    def more(self, other_card):
        return self.__cost() > other_card.__cost()

    def __gt__(self, other):
        return self.more(other)

    def less(self, other_card):
        return self.__cost() < other_card.__cost()

    def __lt__(self, other):
        return self.less(other)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def show(self):
        return f"deck[{len(self.cards)}] {', '.join([card.to_str() for card in self.cards])}"

    def __str__(self):
        return f"deck[{len(self.cards)}] {', '.join([card.to_str() for card in self.cards])}"

    def draw(self, x):
        res = self.cards[:x]
        self.cards = self.cards[x:]
        return res

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):
        self.cards = self.cards[num_card:] + self.cards[:num_card]


deck = Deck()
print("# 1. Вывод колоды в терминал: ")
print(deck)  # вместо print(deck.show())

card1, card2 = deck.draw(2)
print("# 2. Вывод карты в терминал: ")
print(card1)  # вместо print(card1.to_str())

print("# 3. Сравнение карт: ")
if card1 > card2:
    print(f"{card1} больше {card2}")
if card1 < card2:
    print(f"{card1} меньше {card2}")

print("# 4. Итерация по колоде: ")
for card in deck:
    print(card, end=" ")
print()

print("# 5. Просмотр карты в колоде по ее индексу: ")
print(deck[6])

# Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
