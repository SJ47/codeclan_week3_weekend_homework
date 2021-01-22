class Game:

    def select_winner(self, player1, player2):
        # Create a list of valid choices
        valid_choices = ["rock", "paper", "scissors"]

        # Stop checking if either player made an invalid entry
        if (player1.choice) not in valid_choices:
            return "Invalid Choices Made by Player 1 - Try Again"
        
        if (player2.choice) not in valid_choices:
            return "Invalid Choices Made by Player 2 - Try Again"
        
        # Find the winner
        winner = "something went wrong in finding a winner"
        
        # check if it is a DRAW
        if player1.choice == player2.choice:
            winner = "Draw"
            return winner
        
        # Check for winner if player1 has ROCK
        winner = player1.name
        if player1.choice == "rock":
            if player2.choice == "paper":
                winner = player2.name
        # Check for winner if player1 has PAPER
        elif player1.choice == "paper":
            if player2.choice == "scissors":
                winner = player2.name
        # Check for winner if player1 has SCISSORS
        elif player1.choice == "scissors":
            if player2.choice == "rock":
                winner = player2.name
       
        # return winner 
        return winner