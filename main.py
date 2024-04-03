class Player:
    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole


class TicTacToe:
    def __init__(self, player):
        self.game = [None, None, None, None, None, None, None, None, None]
        self.playerToPlay = player


    def play(self, caseNumber, symbole):
        if(self.game[caseNumber] == None):
            self.game[caseNumber] = symbole
        else:
            raise ValueError("Case already played !")






