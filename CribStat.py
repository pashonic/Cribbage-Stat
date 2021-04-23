#
# Cribbage Stat Copyright (C) 2012  Aaron Greene
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Visit https://github.com/pashonic/SVNDistribution for addtional documentation.
#

from random import choice
import itertools
import sys
import time

Suits = ['spade', 'club', 'heart', 'diamond']
Faces = {'ace' :{'value':1, 'order':1},
         '2' :{'value':2, 'order':2},
         '3' :{'value':3, 'order':3},
         '4' :{'value':4, 'order':4},
         '5' :{'value':5, 'order':5},
         '6' :{'value':6, 'order':6},
         '7' :{'value':7, 'order':7},
         '8' :{'value':8, 'order':8},
         '9' :{'value':9, 'order':9},
         '10' :{'value':10, 'order':10},
         'jack' :{'value':10, 'order':11},
         'queen':{'value':10, 'order':12},
         'king' :{'value':10, 'order':13}}

class CardSet:

    def __init__(self, cardList = []):
        self.Cards = list(cardList)
        self.CutCard = None

    def __add__(self, otherCards):
        newCardSet = CardSet()
        newCardSet.Cards = list(self.Cards + otherCards.Cards)
        return newCardSet

    def __eq__(self, otherCards):
        return (sorted(self.Cards) == sorted(otherCards.Cards))

    def SetCutCard(self, card):
        self.CutCard = dict(card)

    def IsCutCard(self, card):
        return (str(card) == str(self.CutCard))

    def CreateDeck(self):
        for face in Faces:
            for suit in Suits:
                self.Cards.append({'face':face, 'suit':suit})
        return self

    def ShowCards(self):
        for card in self.Cards:
            print (card['face'] + '|' + card['suit'])

    def DealCards(self, numberOfCards):
        newCardSet = CardSet()
        for cardNumber in range(numberOfCards):
            card = choice(self.Cards)
            self.Cards.remove(card)
            newCardSet.Cards.append(card)
        return newCardSet

    def Get15Score(self):
        returnTotal = 0
        for i in range(2, len(self.Cards) + 1):
            for cards in list(itertools.combinations(self.Cards, i)):
                sum = 0
                for card in cards:
                    sum += Faces[card['face']]['value']
                if (sum == 15):
                    returnTotal += 2
        return returnTotal

    def GetPairScore(self):
        returnTotal = 0
        for face in Faces:
            count = 0
            for card in self.Cards:
                if card['face'] == face:
                    count += 1
            returnTotal += (count - 1) * count
        return returnTotal

    def GetBestWorstCards(self, bestCount):
        highScore = -1
        returnLowCardSet = None
        returnHighCardSet = None
        for bestCardsCandidates in itertools.combinations(self.Cards, bestCount):

            #
            # Get worst cards.
            #

            worstCardsCandidates = []
            for cardA in self.Cards:
                if not cardA in bestCardsCandidates:
                    worstCardsCandidates.append(cardA)

            #
            # Calculate best cards candidate.
            #

            cardSet = CardSet(bestCardsCandidates)
            cardSetScore = cardSet.GetScore()
            if (cardSetScore > highScore):
                returnHighCardSet = CardSet(bestCardsCandidates)
                returnLowCardSet = CardSet(worstCardsCandidates)
                highScore = cardSetScore
        return returnHighCardSet, returnLowCardSet


    def GetFlushScore(self):
        returnTotal = 0
        suitList = []
        cardCopyList = list(self.Cards)

        #
        # Remove cut card if it is defined.
        #

        if not (self.CutCard == None):
            cardCopyList.remove(self.CutCard)

        #
        # Create suit list.
        #

        for card in cardCopyList:
            suitList.append(card['suit'])

        #
        # Check if all cards are same suit.
        #

        suitSet = set(suitList)
        if (len(suitSet) < 2):
            returnTotal = len(cardCopyList)

            #
            # Add point if cut card is same suit.
            #

            if not (self.CutCard == None) and(self.CutCard['suit'] == list(suitSet)[0]):
                returnTotal += 1
        return returnTotal

    def GetNobScore(self):
        if (self.CutCard == None):
            return 0
        for card in self.Cards:
            if (card['face'] == 'jack'):
                if (card['suit'] == self.CutCard['suit']):
                    return 1
        return 0

    def GetRunScore(self):
        returnTotal = 0
        for runSize in reversed(range(3, len(self.Cards) + 1)):
            for cards in list(itertools.combinations(self.Cards, runSize)):
                orderList = []

                #
                # Create order list.
                #

                for card in cards:
                    orderList.append(Faces[card['face']]['order'])

                #
                # Determine if current combination is run.
                #

                isRun = True
                num = None
                for item in sorted(orderList):
                    if not (num == None):
                        if ((item - num) != 1):
                            isRun = False
                            break
                    num = item
                if not isRun:
                    continue

                #
                # This is a run so add it to score.
                #

                returnTotal += runSize
            if (returnTotal > 0):
                return returnTotal
        return returnTotal

    def GetScore(self):
        return self.Get15Score() +\
               self.GetRunScore() +\
               self.GetPairScore() +\
               self.GetNobScore() +\
               self.GetFlushScore()

total15Score = 0
totalRunScore = 0
totalPairScore = 0
totalNobScore = 0
totalFlushScore = 0
sampleCount = 50
startTime = time.time()
for samples in range(sampleCount):

    #
    # Create deck.
    #

    cardDeck = CardSet().CreateDeck()

    #
    # Deal 6 cards.
    #

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

    total15Score += cardHand.Get15Score()
    totalRunScore += cardHand.GetRunScore()
    totalPairScore += cardHand.GetPairScore()
    totalNobScore += cardHand.GetNobScore()
    totalFlushScore += cardHand.GetFlushScore()

#
# Show results.
#

rightJust = 20
totalScore = total15Score + totalRunScore + totalPairScore + totalNobScore + totalFlushScore
print ('{0}{1}'.format('Average Score:'.ljust(rightJust), (totalScore / float(sampleCount))))
