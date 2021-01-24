import random
class Game:

    # Class scoped variable for all instance functions to access
    # Create a list of valid choices
    valid_choices = ["rock", "paper", "scissors"]

    # Function will return the winner after comparing both players choices
    @classmethod    
    def select_winner(cls, player1, player2):
        # Stop checking if either player made an invalid entry (for MVP exercise)     
        if ((player1.choice.lower()) not in cls.valid_choices or (player2.choice.lower()) not in cls.valid_choices):
            return "Invalid Choices Made - Try Again"

        ### Find the winner      
        # check if it is a DRAW and return none - no winner
        if player1.choice.lower() == player2.choice.lower():
            return None
        
        # default winner just to have a value
        winner = player1.name

        # Check for winner if player1 has ROCK
        if (player1.choice.lower() == "rock" and player2.choice.lower() == "paper"):
                winner = player2.name
        # Check for winner if player1 has PAPER
        elif (player1.choice.lower() == "paper" and player2.choice.lower() == "scissors"):
                winner = player2.name
        # Check for winner if player1 has SCISSORS
        elif (player1.choice.lower() == "scissors" and player2.choice.lower() == "rock"):
                winner = player2.name
       
        # return winner 
        return winner

    # Return random choice for computer
    @classmethod
    def select_computer_random_choice(cls):
        return random.choice(cls.valid_choices)

