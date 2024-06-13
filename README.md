Card Game Simulation in Python

This is a simple card game simulation in Python. The game is played between two players, and the goal is to collect cards of the same rank and number. The game ends when one player's card list is empty.

Gameplay

The game starts with a deck of 40 cards, each with a unique rank and number. The deck is shuffled, and the cards are distributed between two players, odam1 and odam2. Each player's hand is displayed, and the user is asked to input the desired card's rank and number.

The game continues until one player's hand is empty. The user's card is compared with the opponent's card, and the winner is determined based on the rank and number of the cards. If the user's card wins, it is added to their hand; otherwise, it is added to the opponent's hand.

Functions

The game has several functions:

aralashtirib_ikkiga_bolish: Shuffles the deck and distributes it between two players.
karta_bormi: Checks if a card is in a list.
ishlatish: The main game loop, which draws a card from each player's hand, asks the user to input the desired card's rank and number, and then checks if the user's card wins.
Classes

The game has two classes:

Karta: Represents a card with a rank and number.
Kartalar: Represents a deck of cards.
Running the Game

To run the game, simply execute the code in a Python interpreter or save it to a file and run it using python. The output will be either "Siz yutdingiz!" (You win!) or "Odam 1 yutdi!" (Odam 1 wins!).

Note: This is a simple simulation, and you may want to add more features to make the game more interesting.