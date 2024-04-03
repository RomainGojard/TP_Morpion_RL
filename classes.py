import random


class Player:
    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole


class TicTacToe:
    def __init__(self, player1, player2):
        self.game = [None, None, None, None, None, None, None, None, None]
        self.playerToPlay = player1
        self.otherPlayer = player2

    def play(self, caseNumber, player):
        if (self.game[caseNumber] == None):
            self.game[caseNumber] = player.symbole
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
        else:
            raise ValueError("L'emplacement n'a jamais été joué ou n'a pas été joué par vous")

    # returns the positions of the empty tiles (= playable positions)
    def allowed_moves(self):
        return [index for index, valeur in enumerate(self.game) if valeur is None]
    
    def opponent_random(self):
        rdmNumber = random.sample(self.allowed_moves(),1)
        self.game[rdmNumber[0]] = self.otherPlayer.symbole
        self.__str__()

