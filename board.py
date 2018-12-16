class board():

    def __init__(self, h, w, _mat=[]):
        self.h = h
        self.w = w
        self._mat = _mat

    def inv_board(self):
        for i in range(17):
            self._mat.append([])

        for i in range(17):
            for j in range(40):
                self._mat[i].append(' ')

        for i in range(self.h):
            self._mat[i][0] = '|'
            self._mat[i][self.w - 1] = '|'
            for j in range(self.w):
                self._mat[0][j] = '-'
                self._mat[self.h - 1][j] = '-'
        self._mat[15][1] = u'\U0001f6e6'
        self._mat[1][20] = 'SPACE'
        self._mat[1][21] = 'INVADERS'

        self._mat[2][21] = 'beware'
        self._mat[2][22] = 'the'
        self._mat[2][23] = 'invasion'

        self._mat[4][21] = 'CONTROLS:'

        self._mat[6][21] = 'q'
        self._mat[6][22] = ':'
        self._mat[6][24] = 'quit'

        self._mat[7][21] = 'a'
        self._mat[7][22] = ':'
        self._mat[7][24] = '<-'

        self._mat[8][21] = 'd'
        self._mat[8][22] = ':'
        self._mat[8][24] = '->'

        self._mat[9][21] = 'spacebar'
        self._mat[9][22] = ':'
        self._mat[9][23] = 'shoot missile'

        self._mat[10][21] = 's'
        self._mat[10][22] = ':'
        self._mat[10][23] = 'spl missile'

        self._mat[14][21] = 'Score'
        self._mat[14][22] = ':'

    def initial(self):
        self._mat[15][1] = ' '
        self._mat[4][3] = 'S'
        self._mat[4][4] = 'P'
        self._mat[4][5] = 'A'
        self._mat[4][6] = 'C'
        self._mat[4][7] = 'E'
        self._mat[5][6] = 'I'
        self._mat[5][7] = 'N'
        self._mat[5][8] = 'V'
        self._mat[5][9] = 'A'
        self._mat[5][10] = 'D'
        self._mat[5][11] = 'E'
        self._mat[5][12] = 'R'
        self._mat[5][13] = 'S'
        self._mat[10][2] = 'P'
        self._mat[10][3] = 'r'
        self._mat[10][4] = 'e'
        self._mat[10][5] = 's'
        self._mat[10][6] = 's'
        self._mat[10][8] = 'a'
        self._mat[10][9] = 'n'
        self._mat[10][10] = 'y'
        self._mat[10][12] = 'k'
        self._mat[10][13] = 'e'
        self._mat[10][14] = 'y'
        self._mat[12][5] = 't'
        self._mat[12][6] = 'o'
        self._mat[12][8] = 's'
        self._mat[12][9] = 't'
        self._mat[12][10] = 'a'
        self._mat[12][11] = 'r'
        self._mat[12][12] = 't'

    def update(self):
        for i in range(self.h):
            for j in range(self.w):
                self._mat[i][j] = ' '

        for i in range(self.h):
            self._mat[i][0] = '|'
            self._mat[i][self.w - 1] = '|'
            for j in range(self.w):
                self._mat[0][j] = '-'
                self._mat[self.h - 1][j] = '-'
        self._mat[15][1] = u'\U0001f6e6'

    def inv_print(self, score):
        for i in range(17):
            for j in range(40):
                if j == 23 and i == 14:
                    print(score, end=' ')
                else:
                    print(self._mat[i][j], end=' '),
            print("")

    def updatemissile(self, oldx, oldy, x, y, sym, spcsym):
        if oldx == 15:  # 8
            self._mat[oldx][oldy] = spcsym
        else:
            self._mat[oldx][oldy] = ' '
        if x == 0:
            self._mat[x][y] = '-'
        else:
            self._mat[x][y] = sym
        for i in range(17):
            self._mat[16][i] = '-'

    def updatespaceship(self, oldx1, oldy1, x1, y1, sym):
        self._mat[oldx1][oldy1] = ' '
        self._mat[x1][y1] = sym

    def updatealien(self, x2, y2, sym):
        self._mat[x2][y2] = sym
