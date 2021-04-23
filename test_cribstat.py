import CribStat

def test_basic():

    cardDeck = CribStat.CardSet().CreateDeck()

    cardHand = cardDeck.DealCards(6)

    #
    # Get the best 4 cards that result in hightest score.
    #

    cardHand = cardHand.GetBestWorstCards(4)[0] # 0 = best cards.

    #
    # Deal cut card.
    #

    cutcard = cardDeck.DealCards(1)
    cardHand += cutcard
    cardHand.SetCutCard(cutcard.Cards[0])

    #
    # Get score.
    #

    score = cardHand.Get15Score()


    assert(30 < 20)