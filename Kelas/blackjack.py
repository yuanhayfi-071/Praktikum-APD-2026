class Card:
    def __init__(self, s, r):
        self.suit = s
        self.rank = r

    def __str__(self):
        return f"{self.rank}{self.suit}"

c = Card("Spades", "Ace")
print(c)

from card import Card
from random import shuffle

class Deck:
    ranks = ["A","2","3","4","5","6","7","8","9","10","K","Q","J"]
    suits = ["♠","♥","♦","♣"]

    def __init__(self):
        self.cards = []

        for r in Deck.ranks:
            for s in Deck.suits:
                self.cards.append(Card(s,r))

    def shuffle(self):
        shuffle(self.cards)

from deck import Deck

class Decks(Deck):
    def __init__(self, numDecks):
        self.cards = []

        for i in range(numDecks):
            d = Deck()

            for card in d.cards:
                self.cards.append(card)

class Player:
    def __init__(self):
        self.money = 1000
        self.hand = []

    def getHand(self):
        return self.hand

    def recieveCard(self,card):
        self.hand.append(card)

    def printHand(self):
        print("Current Hand:", *self.hand)

    def clearHand(self):
        self.hand = []

    def getMoney(self):
        return self.money

    def setMoney(self, newMoney):
        self.money = newMoney

from player import Player

class Dealer(Player): #so dealer inherts the player
    def printHand(self, round_num=0):
        if round_num == 1:
            print("Dealer's Hand:", self.hand[1])
        else:
            print("Dealer's Hand:" *self.hand)

from deck import Deck
from desks import Decks
from player import Player
from dealer import Dealer
from time import sleep

values = dict(zip(Deck.ranks, [11,2,3,4,5,6,7,8,9,10,10,10,10]))