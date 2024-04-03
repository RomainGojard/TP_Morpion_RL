class Player:
    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole


class TicTacToe:
    def __init__(self, player):
        self.game = [None, None, None, None, None, None, None, None, None]
        self.playerToPlay = player

    def play(self, caseNumber, symbole):
        if (self.game[caseNumber] == None):
            self.game[caseNumber] = symbole
        else:
            raise ValueError("Case already played !")

    def __str__(self):
        conv = lambda i: i or ' '
        res = [conv(i) for i in self.game]
        print(" | " + str(res[0]) + " | " + str(res[1]) + " | " + str(res[2]) + " | \n" +
              " | " + str(res[3]) + " | " + str(res[4]) + " | " + str(res[5]) + " | \n" +
              " | " + str(res[6]) + " | " + str(res[7]) + " | " + str(res[8]) + " | \n")

    def has_winner(self):
        WIN_SCHEMES = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        t = self.game
        result = False
        for win_scheme in WIN_SCHEMES:
            if t[win_scheme[0]] == t[win_scheme[1]] == t[win_scheme[2]]:
                result = True
                break

        return result
    
    def reset(self, _player):
        self.game = [None, None, None, None, None, None, None, None, None]
        self.playerToPlay = _player

    def is_draw(self):
        if ((None in self.game) or self.has_winner()):
            return False
        else:
            return True

    def undo(self, caseNumber, player):
        if (self.game[caseNumber] == player.symbole):
            self.game[caseNumber] = None
        else :
            raise ValueError("L'emplacement n'a jamais été joué ou n'a pas été joué par vous")



player = Player("test-user", "X")
game = TicTacToe(player)
game.__str__()
