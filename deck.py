import random
from enum import Enum


class Suit(Enum):
    DIAMONDS = 1
    SPADES = 2
    HEARTS = 3
    CLUBS = 4


class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank.name + " of " + self.suit.name


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def count_suit(self, suit):
        count = 0
        for card in self.cards:
            if card.suit == suit:
                count += 1
        return count

    def count_rank(self, rank):
        count = 0
        for card in self.cards:
            if card.rank == rank:
                count += 1
        return count



class StandardDeck(Deck):
    def __init__(self):
        cards = []
        for rank in Rank:
            for suit in Suit:
                cards.append(Card(rank, suit))
        super().__init__(cards)


class AbandonedDeck(Deck):
    def __init__(self):
        cards = []
        for rank in Rank:
            if rank == Rank.JACK:
                continue
            if rank == Rank.QUEEN:
                continue
            if rank == Rank.KING:
                continue
            for suit in Suit:
                cards.append(Card(rank, suit))
        super().__init__(cards)


if __name__ == '__main__':
    standard_deck = StandardDeck()
    abandoned_deck = AbandonedDeck()
    print(standard_deck.draw())
    ...
