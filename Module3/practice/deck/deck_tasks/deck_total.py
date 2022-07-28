import random


class Card:
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"
    SPADES = "Spades"
    CLUBS = "Clubs"

    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    @property
    def to_str(self):
        suit_icons = {"Diamonds": '\u2662', "Hearts": '\u2661', "Spades": '\u2660', "Clubs": '\u2663'}
        return f"{self.value}{suit_icons[self.suit]}"

    def __str__(self):
        return self.to_str

    def __repr__(self):
        return self.__str__()

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    @property
    def __cost(self):
        suit_cost = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}
        values_cost = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                       'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return values_cost[self.value] * 4 + suit_cost[self.suit]

    def more(self, other_card):
        return self.__cost > other_card.__cost

    def __gt__(self, other):
        return self.more(other)

    def less(self, other_card):
        return self.__cost < other_card.__cost

    def __lt__(self, other):
        return self.less(other)


class Deck:
    # Список карт в колоде. Каждым элементом списка будет объект класса Card
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

    def __init__(self):
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(value, suit))

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def show(self):
        return f"deck[{len(self.cards)}] {', '.join([str(card) for card in self.cards])}"

    def __str__(self):
        return f"deck[{len(self.cards)}] {', '.join([str(card) for card in self.cards])}"

    def draw(self, x):
        res = self.cards[:x]
        self.cards = self.cards[x:]
        return res

    def shuffle(self):
        random.shuffle(self.cards)

    def shift(self, num_card):
        self.cards = self.cards[num_card:] + self.cards[:num_card]


# В этом файле дорабатываем классы, если это требуется для решения задачи
# Важно! При доработке классов для решение очередной задачи, необходимо не сломать решение предыдущей

if __name__ == "__main__":
    # Тут можно разместить тесты классов
    ...
