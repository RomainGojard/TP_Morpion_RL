from classes import Player
from classes import TicTacToe

ai_random = Player("AI RANDOM", "X")
player_de_fou = Player("Player de fou malade", "O")
game = TicTacToe(player_de_fou, ai_random)


def main():
    while game.isGameOn:
        print(game.allowed_moves())

        if game.playerToPlay.name == "AI RANDOM":
            game.opponent_random(ai_random)
        else:
            game.opponent_next(player_de_fou, ai_random)

        game.__str__()

        if game.has_winner() or game.is_draw():
            game.end_game()
            game.reset(player_de_fou, ai_random)

        print("Score " + player_de_fou.name + " " + str(player_de_fou.score) + "  |  " + ai_random.name + " " + str(ai_random.score))


main()
