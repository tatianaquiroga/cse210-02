from game.card import Card
import random

x=(random.randint(1,13))
tries=0
guess=0

class Director:

    """The player who is playing the game.
    
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        points (int): The current points of the player.
        cards (List[Card]): A list of Card instances.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = True
        
        self.points = 300
        
        self.cards = []
        
        # Create 13 Card objects and append them to the cards list
        for i in range(13):
            self.cards.append(cards())

    def start_game(self):
        print("Hello, this is HILO game")
        print("You start with 300 points")
        print("You have to guess if the next card is lower or higher")
        print("Let's start!!!")
        print("------------------------------------------")

        while guess != x :
            tries= tries + 1
            guess= int(input("What is your guess? "))

            if guess > x:
                print("Sorry your guess was too high.")
            if guess < x:
                print("Sorry your guess was too low.")
            if guess == x: 
                print("Congrats, you are a winner!!")

            if guess == x:
                print(" You won")


            if guess != x:
                print("Sorry, you lose!! The number was",x)
    pass


          
    
