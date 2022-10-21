# Poker-Hand-Recognition

### Creators of the Poker Hand Data Set
Robert Cattral (cattral@gmail.com)\
Franz Oppacher (oppacher@scs.carleton.ca)\
Carleton University, Department of Computer Science\
Intelligent Systems Research Unit\
1125 Colonel By Drive, Ottawa, Ontario, Canada, K1S5B6\

### Data Set Information
Each record is an example of a hand consisting of five playing cards drawn from a standard deck of 52. Each card is described using two attributes (suit and rank), for a total of 10 predictive attributes. There is one Class attribute that describes the "Poker Hand". The order of cards is important, which is why there are 480 possible Royal Flush hands as compared to 4

### Attribute Information
1) S1 "Suit of card #1"
Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

2) C1 "Rank of card #1"
Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

3) S2 "Suit of card #2"
Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

4) C2 "Rank of card #2"
Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

5) S3 "Suit of card #3"
Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

6) C3 "Rank of card #3"
Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

7) S4 "Suit of card #4"
Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

8) C4 "Rank of card #4"
Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

9) S5 "Suit of card #5"
Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}

10) C5 "Rank of card 5"
Numerical (1-13) representing (Ace, 2, 3, ... , Queen, King)

11) CLASS "Poker Hand"
Ordinal (0-9)

0: Nothing in hand; not a recognized poker hand \
1: One pair; one pair of equal ranks within five cards \
2: Two pairs; two pairs of equal ranks within five cards \
3: Three of a kind; three equal ranks within five cards \
4: Straight; five cards, sequentially ranked with no gaps \
5: Flush; five cards with the same suit \
6: Full house; pair + different rank three of a kind \
7: Four of a kind; four equal ranks within five cards \
8: Straight flush; straight + flush \
9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush
