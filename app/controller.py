from app import app
from flask import render_template, request
from app.models.player import Player 
from app.models.game import Game

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/play', methods=["POST"])
def play():
    return render_template('play.html', title='Player 1', name1=request.form['name1'])

@app.route('/rock')
def rock():
    return render_template('player2.html', title='Player 2', choice='rock')

@app.route('/paper')
def paper():
    return render_template('player2.html', title='Player 2', choice='paper')

@app.route('/scissors')
def scissors():
    return render_template('player2.html', title='Player 2', choice='scissors')

@app.route('/<choice1>/<choice2>')
def result(choice1, choice2):
    # namePlayer1 = request.form['name1']
    # namePlayer2 = request.form['name2']
    player_1 = Player("Player 1", choice1)
    player_2 = Player("Player 2", choice2)
    game = Game()
    result = game.check_winner(player_1, player_2)
    return render_template('result.html', result=result, title="The Winner!")