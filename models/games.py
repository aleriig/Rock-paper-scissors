from models.game import *

game1 = Game ("rock", "scissors")
game2 = Game ("paper", "rock")

games = [game1, game2]


def get_winner(player_1, player_2):
        if player_1 == player_2:
            return "None"
        elif player_1 == "rock":
            if player_2== "scissors":
                return "Player 1 wins!"
            else:
                return "player 2 wins"
        elif player_1 == "scissors":
            if player_2 == "paper":
                return "Player1 wins"
            else:
                return "Player 2 wins"
        elif player_1 == "paper":
            if player_2 == "rock":
                return "Player 1 wins"
            else:
                return "Player 2 wins"