from random import randint

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank == 1:
            self.value = 'Ace'
        elif rank == 11:
            self.value = 'Jack'
        elif rank == 12:
            self.value = 'Queen'
        elif rank == 13:
            self.value = 'King'
        else:
            self.value = str(rank)

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        if self.rank == 10:
            return f"{self.value}{self.suit[0]}"
        return f"{self.value[0]}{self.suit[0]}"

class Deck():

    def __init__(self):

        self.suits = ['clubs', 'hearts', 'diamonds', 'spades']
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        self.contents = [] # gonna put cards here

        for suit in self.suits:
            for rank in self.ranks:
                self.contents.append(Card(suit, rank))

        self.shuffle_deck()

    def shuffle_deck(self):

        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    def deal_card(self):
        if len(self.contents) != 0:
            return self.contents.pop()
        else:
            return None

new_deck = Deck()

player_1 = []
player_2 = []
player_3 = []
player_4 = []
player_5 = []

players = [player_1, player_2, player_3, player_4, player_5]

for player in players:
    player.append(new_deck.deal_card())
for player in players:
    player.append(new_deck.deal_card())

for player in players:
    print(player)
