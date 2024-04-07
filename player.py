import matplotlib.pyplot as plt
import numpy as np

from game import Game
from deck import StandardDeck, AbandonedDeck
from deck import Suit, Rank
from hands import straights
from probabilities import prob_to_draw_rank

def count_suit(cards, suit):
    count = 0
    for card in cards:
        if card.suit == suit:
            count += 1
    return count


def count_rank(cards, rank):
    count = 0
    for card in cards:
        if card.rank == rank:
            count += 1
    return count


class Player:
    def __init__(self, game):
        self.game = game

    def fish_for_flush(self):
        while True:
            # Count the suits
            suit_counts = {}
            for suit in Suit:
                suit_counts[suit] = count_suit(self.game.hand, suit)

            # Evaluate the best suits to focus on
            # todo: this should look at the deck and calculate probabilities, not just take the maximum as we're doing now
            max_value = -1
            max_suit = None
            for suit in suit_counts:
                if suit_counts[suit] > max_value:
                    max_value = suit_counts[suit]
                    max_suit = suit

            if max_value >= 5:
                return

            # Discard cards that don't match this suit
            cards_to_discard = []
            for card in self.game.hand:
                if card.suit != max_suit and len(cards_to_discard) < self.game.max_cards_per_discard:
                    cards_to_discard.append(card)
            self.game.discard(cards_to_discard)

    def fish_for_hands(self, target_hands):
        while True:
            cards_to_keep = None
            highest_prob = 0.0
            for target_hand in target_hands:
                ranks_to_match = target_hand.copy()
                matching_cards = []
                for target_rank in target_hand:
                    for card in self.game.hand:
                        if (card.rank == target_rank) & ranks_to_match.__contains__(card.rank):
                            matching_cards.append(card)
                            ranks_to_match.remove(card.rank)

                num_draws = min(self.game.max_cards_per_discard, len(self.game.hand) - len(matching_cards))
                prob = 1.0
                for rank in ranks_to_match:
                    prob *= prob_to_draw_rank(self.game.deck, rank, num_draws)

                if prob > highest_prob:
                    highest_prob = prob
                    cards_to_keep = matching_cards

            if len(cards_to_keep) == 5:
                return

            cards_to_discard = []
            for card in self.game.hand:
                if (len(cards_to_discard) < self.game.max_cards_per_discard) & (not cards_to_keep.__contains__(card)):
                    cards_to_discard.append(card)

            self.game.discard(cards_to_discard)


if __name__ == '__main__':
    num_games = 10000
    num_discards = []
    for _ in range(num_games):
        player = Player(Game(StandardDeck()))
        player.fish_for_hands(straights)
        num_discards.append(player.game.discards)
    plt.hist(num_discards, bins=np.arange(-0.5, 10.5), edgecolor='k', density=True, alpha=0.25, label='Straights')

    num_discards = []
    for _ in range(num_games):
        player = Player(Game(StandardDeck()))
        player.fish_for_flush()
        num_discards.append(player.game.discards)
    plt.hist(num_discards, bins=np.arange(-0.5, 10.5), edgecolor='k', density=True, alpha=0.25, label='Flushes')
    plt.title('Standard Deck')
    plt.ylabel('Probability')
    plt.xlabel('Number of Discards')
    plt.legend()
    plt.show()