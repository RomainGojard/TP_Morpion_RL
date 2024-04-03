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
    
    def __str__(self):
        conv = lambda i : i or ' '
        res = [conv(i) for i in self.game]
        print(" | " + str(res[0]) + " | " + str(res[1]) + " | " + str(res[2]) + " | \n" +
              " | " + str(res[3]) + " | " + str(res[4]) + " | " + str(res[5]) + " | \n" +
              " | " + str(res[6]) + " | " + str(res[7]) + " | " + str(res[8]) + " | \n")

player = Player("test-user","X")
game = TicTacToe(player)
game.__str__()





