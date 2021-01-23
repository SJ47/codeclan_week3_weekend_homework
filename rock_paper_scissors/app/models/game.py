import random
class Game:

    # Class scoped variable for all instance functions to access
    # Create a list of valid choices
    valid_choices = ["rock", "paper", "scissors"]

    # Function will return the winner after comparing both players choices
    @classmethod    
    def select_winner(cls, player1, player2):
        
        # valid_choices = ["rock", "paper", "scissors"]

        # Stop checking if either player made an invalid entry
        if (player1.choice.lower()) not in cls.valid_choices:
            return "Invalid Choices Made by Player 1 - Try Again"
        
        if (player2.choice.lower()) not in cls.valid_choices:
            return "Invalid Choices Made by Player 2 - Try Again"
        
        ### Find the winner
       
        # check if it is a DRAW and return none - no winner
        if player1.choice.lower() == player2.choice.lower():
            return None
        
        # Check for winner if player1 has ROCK
        winner = player1.name
        if player1.choice.lower() == "rock":
            if player2.choice.lower() == "paper":
                winner = player2.name
        # Check for winner if player1 has PAPER
        elif player1.choice.lower() == "paper":
            if player2.choice.lower() == "scissors":
                winner = player2.name
        # Check for winner if player1 has SCISSORS
        elif player1.choice.lower() == "scissors":
            if player2.choice.lower() == "rock":
                winner = player2.name
       
        # return winner 
        return winner

    # Return random choice for computer
    @classmethod
    def select_computer_random_choice(cls):
        # valid_choices = ["rock", "paper", "scissors"]
        return random.choice(cls.valid_choices)

