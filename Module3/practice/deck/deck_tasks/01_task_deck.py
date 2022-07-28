from deck_total import Card, Deck


desk = Deck()

desk.shuffle()

card1, card2 = desk.draw(2)

print(f"карта {card1} {'больше' if card1 > card2 else 'меньше'} {card2}")
