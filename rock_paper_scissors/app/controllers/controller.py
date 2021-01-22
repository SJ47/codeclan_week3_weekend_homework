from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<player1_choice>/<player2_choice>")
def get_player_choices(player1_choice, player2_choice):
    player1 = Player("Fred", player1_choice)
    player2 = Player("Barney", player2_choice)

    # Check for the winner
    check_for_winner = Game()
    winner = check_for_winner.select_winner(player1, player2)
    
    # Return the result
    return render_template("result.html", player1=player1, player2=player2, winner = winner)