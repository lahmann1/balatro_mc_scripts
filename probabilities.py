from deck import StandardDeck, AbandonedDeck, Deck, Card, Rank, Suit


def prob_to_draw_rank(deck, rank, num_draws):
    prob = 0.0
    num_cards = deck.count_rank(rank)
    if num_draws == 0:
        return 0
    for i in range(num_draws):
        if i >= len(deck.cards):
            continue
        prob += num_cards / (len(deck.cards) - i) * (1 - prob_to_draw_rank(deck, rank, i))
    return prob


if __name__ == '__main__':
    deck = AbandonedDeck()
    test_deck = Deck(
        [
            Card(Rank.ACE, Suit.HEARTS),
            Card(Rank.ACE, Suit.HEARTS),
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.THREE, Suit.HEARTS),
        ]
    )
    print(prob_to_draw_rank(test_deck, Rank.ACE, 10))