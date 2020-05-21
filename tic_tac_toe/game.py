import random
from copy import deepcopy
from board import Board
from btree import LinkedBinaryTree
from btnode import BSTNode

class NotEmptyCellError(Exception):
    pass

class IndexOutOfRangeError(Exception):
    pass

class Game():
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

    def win_check(self, board):
        check = board.check_board()
        if check is not None:
            return check

    def tree_creation(self, board, count, tree, move, possible):
        # print(possible)
        if self.win_check(board) == 'x':
            count += 1
            return count
        if len(possible) == 1:
            print('h')
            board.add_move(possible[0][0], possible[0][1], move)
            tree.insert_left = board
            return count
        else:
            if move == 'x':
                next_move = 'o'
            else:
                next_move = 'x'
            if not possible:
                return count
            move1 = random.choice(possible)
            possible.remove(move1)
            board1 = deepcopy(board)
            board1.add_move(move1[0], move1[1], move)
            tree.insert_left(board1)

            move2 = random.choice(possible)
            possible.remove(move2)
            board2 = deepcopy(board)
            board2.add_move(move2[0], move2[1], move)
            tree.insert_right(board2)

            count += self.tree_creation(board1, count, tree.get_left_child(),
                                        next_move, possible)
            count += self.tree_creation(board2, count, tree.get_right_child(),
                                        next_move, possible)

        return count

    def game(self):
        while True:
            print(self.board)
            winner = self.win_check(self.board)
            if winner:
                print(winner)
            possible = self.possible_moves(self.board)
            user = int(input('Enter a number(0 to 8): '))
            if not(0 <= user <= 8):
                raise NotEmptyCellError('Please, enter valid index')
            row, col = user//3, user % 3
            if self.board.is_empty(col, row):
                self.board.add_move(col, row, 'o')
            else:
                raise IndexOutOfRangeError('This cell is not empty')
            if len(possible) == 1:
                self.board.add_move(possible[0][0], possible[0][1], 'x')
                return self.board.check_board()
            # if len(possible) == 2:
            #     self.board.add_move(possible[0][0], possible[0][1], 'x')
            #     return self.board.check_board()
            node = BSTNode(self.board)
            tree = LinkedBinaryTree(node)

            # possible = self.possible_moves(self.board)
            move1 = random.choice(possible)
            possible.remove(move1)
            # self.board.remove_move(move1[1], move1[0])
            board1 = deepcopy(self.board)
            board1.add_move(move1[0], move1[1], 'x')
            tree.insert_left(board1)
            tree1 = self.tree_creation(
                board1, 0, tree.get_left_child(), 'x', possible)
            print(possible, 'p')
            possible = self.possible_moves(self.board)
            if move1 in possible:
                possible.remove(move1)
            print(possible, 'p')
            if possible:
                print('e')
                move2 = random.choice(possible)
                # self.board.remove_move(move2[1], move2[0])
                possible.remove(move2)
                board2 = deepcopy(self.board)
                board2.add_move(move2[0], move2[1], 'x')
                tree.insert_right(board2)
                print(move1, move2, 'm')
                tree2 = self.tree_creation(
                    board1, 0, tree.get_right_child(), 'x', possible)
                possible = self.possible_moves(self.board)
                print(tree1, tree2, possible)
                if tree1 > tree2:
                    self.board = board1
                else:
                    self.board = board2
                print(possible)
            else:
                self.board = board1
            winner = self.win_check(self.board)
            print(winner)
            if winner:
                print(self.board)
                print(winner)
                return


if __name__ == '__main__':
    game = Game()
