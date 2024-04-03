from classes import Player
from classes import TicTacToe


ai = Player("AI", "X")
player = Player("Player", "O")
game = TicTacToe(player,ai)

def main() :
    while game.isGameOn:
        if game.playerToPlay.name == "AI":
            game.opponent_random()




#main()

