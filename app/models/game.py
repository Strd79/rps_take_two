from app.models.player import Player 

class Game:

    def check_winner(self, player_1, player_2):
        if player_1.choice == 'rock' and player_2.choice == 'scissors':
            return f"{player_1.name} WINS with {player_1.choice.capitalize()}!"
        elif player_1.choice == 'rock' and player_2.choice == 'paper':
            return f"{player_2.name} WINS with {player_2.choice.capitalize()}!"
        elif player_1.choice == 'paper' and player_2.choice == 'rock':
            return f"{player_1.name} WINS with {player_1.choice.capitalize()}!"
        elif player_1.choice == 'paper' and player_2.choice == 'scissors':
            return f"{player_2.name} WINS with {player_2.choice.capitalize()}!"
        elif player_1.choice == 'scissors' and player_2.choice == 'paper':
            return f"{player_1.name} WINS with {player_1.choice.capitalize()}!"
        elif player_1.choice == 'scissors' and player_2.choice == 'rock':
            return f"{player_2.name} WINS with {player_2.choice.capitalize()}!"
        else:
            return "It's a draw, play again!"