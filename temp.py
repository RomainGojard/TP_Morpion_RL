class TicTacToe:
    def has_winner(self):
        WINS = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,4,8],
            [2,4,6]
        ]
        t = self.game
        for win_scheme in WINS:
            if t[win_scheme[0]] == t[win_scheme[1]] == t[win_scheme[2]]:
                return True



