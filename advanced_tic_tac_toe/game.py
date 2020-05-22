import random
from copy import deepcopy
from board import Board
from btree import LinkedTree
from btnode import BSTNode


class NotEmptyCellError(Exception):
    pass


class IndexOutOfRangeError(Exception):
    pass


class Game:
    """Initializes the game"""

    def __init__(self):
        """Initializes the board and starts the game"""
        self.board = Board()
        self.game()

    def possible_moves(self, board):
        """Returns the list of possible moves"""
        rows, cols = 3, 3
        possible = []
        for row in range(rows):
            for col in range(cols):
                if board.is_empty(col, row):
                    possible.append((row, col))
        return possible

    def tree_creation(self, board, count, tree, move, possible):
        """Returns the number of winning combinations"""
        if len(possible) == 1:
            board.add_move(possible[0][1], possible[0][0], move)
            tree.insert_left = board
            if board.check_board() == 'x':
                count += 1
            return count
        if board.check_board() == 'x':
            count += 1
            return count
        else:
            if move == 'x':
                next_move = 'o'
            else:
                next_move = 'x'
            if not possible:
                return count
            i, j = 0, 0
            while possible:
                move1 = random.choice(possible)
                possible.remove(move1)
                board1 = deepcopy(board)
                board1.add_move(move1[1], move1[0], move)
                tree.insert_node(board1, True)
                possible2 = deepcopy(possible)

                count += self.tree_creation(board1, count, tree.get_children(i),
                                            next_move, possible)
                i = j
                j += 1
        return count

    def game(self):
        """Runs the game"""
        while True:
            print(self.board)

            possible = self.possible_moves(self.board)
            user = int(input('Enter a number(0 to 8): '))
            if not(0 <= user <= 8):
                raise NotEmptyCellError('Please, enter valid index')
            row, col = user//3, user % 3
            if self.board.is_empty(col, row):
                self.board.add_move(col, row, 'o')
            else:
                raise IndexOutOfRangeError('This cell is not empty')
            possible = self.possible_moves(self.board)

            winner = self.board.check_board()
            if winner:
                print(self.board)
                print(winner + ' won the game!')
                break
            winner = self.board.check_board()
            if winner:
                print(winner + ' won the game!')
                break
            node = BSTNode(self.board)
            tree = LinkedTree(node)

            i, j = 0, 0
            trees = []
            while possible:
                move1 = random.choice(possible)
                possible.remove(move1)
                board1 = deepcopy(self.board)
                board1.add_move(move1[1], move1[0], 'x')
                tree.insert_node(board1, verbose=True)
                possible1 = deepcopy(possible)
                tree1 = self.tree_creation(
                    board1, 0, tree.get_children(i), 'x', possible1)
                trees.append(tree1)
                i = j
                j += 1
            tr = max(trees)
            ind = trees.index(tr)
            self.board = tree.get_children(ind).key
            winner = self.board.check_board()
            if winner:
                print(self.board)
                print(winner + ' won the game!')
                break


if __name__ == '__main__':
    game = Game()
