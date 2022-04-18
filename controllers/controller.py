from flask import render_template, request, redirect
from app import app
from models.player import *
from models.game import *
from models.games import games, get_winner

@app.route('/')
def index():
    return render_template('index.html', title='Home!')

@app.route('/rock/scissors')
def rock_wins():
    return "Player 1 wins by rock"


@app.route('/games', methods=['POST', 'GET'])
def play_game():
    player1_choice = request.form
    player1_choice = Player("Player 1", 'scissors')
    player2_choice = Player("Player 2", 'rock')
    winner = Game(player1_choice=player1_choice, player2_choice=player2_choice)
    get_winner(winner)
    return render_template('index.html', title='games', games=games)
    
    
@app.route('/welcome', methods= ['POST'])
def instructions():
    return render_template('index.html', title='welcome')

