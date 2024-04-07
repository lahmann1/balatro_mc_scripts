from deck import StandardDeck, AbandonedDeck, Card


class Game:
    def __init__(self, deck, hand_size=8, max_cards_per_discard=5):
        self.deck = deck
        self.hand = [deck.draw() for _ in range(hand_size)]
        self.max_cards_per_discard = max_cards_per_discard
        self.discards = 0

    def discard(self, cards):
        for card in cards:
            self.hand.remove(card)
            self.hand.append(self.deck.draw())
        self.discards += 1


if __name__ == '__main__':
    game = Game(StandardDeck())
    for card in game.hand:
        print(card)
    game.discard([game.hand[0]])
    print()
    for card in game.hand:
        print(card)
