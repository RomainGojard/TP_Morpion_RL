from classes import Player
from classes import TicTacToe

ai = Player("AI", "X")
player = Player("Player", "O")
game = TicTacToe(player, ai)


def main():
    while game.isGameOn:
        print(game.allowed_moves())

        if game.playerToPlay.name == "AI":
            game.opponent_random(ai)
        else:
            game.opponent_next(player, ai)

        game.__str__()

        if game.has_winner() or game.is_draw():
            game.end_game()
            game.reset(ai, player)




main()
