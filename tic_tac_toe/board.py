class Board:

    def __init__(self, first_row=['_', '_', '_'], second_row=['_', '_', '_'],
                 third_row=['_', '_', '_']):
        """Initializes the board as well last step and its symbol"""
        self.first_row = first_row
        self.second_row = second_row
        self.third_row = third_row
        self.board = [first_row, second_row, third_row]

    def __str__(self):
        """Prints the state of the game"""
        rows = [self.first_row,
                self.second_row, self.third_row]
        s = ''
        for row in rows:
            for pos in row:
                s += pos + ' '
            s += '\n'
        return s

    def is_empty(self, ind, row):
        """Returns True if the position is empty and False otherwise"""
        if self.board[row][ind] == '_':
            return True
        return False

    def add_move(self, ind, row, symb):
        """Add new move to the board"""
        if self.board[row][ind] == '_':
            self.board[row][ind] = symb
            return True
        else:
            return False

    def remove_move(self, ind, row):
        """Add new move to the board"""
        self.board[row][ind] = '_'

    def check_board(self):
        """Returns None if there is no winner and the symbol of the winner otherwise"""
        win_x = 'xxx'
        win_o = 'ooo'
        if ''.join(self.first_row) == win_x or ''.join(self.second_row) == win_x \
                or ''.join(self.third_row) == win_x:
            return 'x'
        elif ''.join(self.first_row) == win_o or ''.join(self.second_row) == win_o \
                or ''.join(self.third_row) == win_o:
            return 'o'
        elif self.first_row[0] + self.second_row[1] + self.third_row[2] == win_x:
            return 'x'
        elif self.first_row[0] + self.second_row[1] + self.third_row[2] == win_o:
            return 'o'
        elif self.first_row[2] + self.second_row[1] + self.third_row[0] == win_x:
            return 'x'
        elif self.first_row[2] + self.second_row[1] + self.third_row[0] == win_o:
            return 'o'
        poss = [0, 1, 2]
        for pos in poss:
            if self.first_row[pos] + self.second_row[pos] + self.third_row[pos] == win_x:
                return 'x'
            elif self.first_row[pos] + self.second_row[pos] + self.third_row[pos] == win_o:
                return 'o'
        verbose = True
        for row in range(3):
            for col in range(3):
                if self.is_empty(row, col):
                    verbose = False
        if verbose:
            return 'both'
