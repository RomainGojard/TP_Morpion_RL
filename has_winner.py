class TicTacToe:
    def has_winner(self):
        WIN_SCHEMES = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,4,8],
            [2,4,6]
        ]

        t = self.game
        result = False
        for win_scheme in WIN_SCHEMES:
            if t[win_scheme[0]] == t[win_scheme[1]] == t[win_scheme[2]]:
                result = True
                break

        return result



