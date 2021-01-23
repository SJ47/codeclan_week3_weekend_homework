from flask import render_template, request, redirect, url_for
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route("/")
def index():
    return render_template("index.html")

# Route for MVP portion of homework
@app.route("/<player1_choice>/<player2_choice>")
def get_player_choices(player1_choice, player2_choice):
    player1 = Player("Fred", player1_choice)
    player2 = Player("Barney", player2_choice)

    # Check for the winner
    check_for_winner = Game()
    winner = check_for_winner.select_winner(player1, player2)

    # Return the result
    return render_template("result.html", player1=player1, player2=player2, winner=winner)

# Routes for extensions and further extensions of homework
@app.route("/play")
def play_game():
    return render_template("play_game.html")

@app.route("/play", methods=["POST"])
def get_player1_name():
    player1=Player(request.form["player1_name"], request.form["player1_selection"])

    # Get computer player choice
    game = Game()
    random_choice = game.select_computer_random_choice()
    player2 = Player("Computer", random_choice)
    
    # Check for the winner
    # check_for_winner = Game()
    winner = game.select_winner(player1, player2)

    # return redirect(url_for("play_game", player1_name=player1_name))
    return render_template("play_game.html", player1_name=player1.name, player1_choice=player1.choice, player2_name=player2.name, player2_choice=player2.choice, winner=winner)
    # return render_template("play_game.html", player1=player1, winner=winner, player2=player2)