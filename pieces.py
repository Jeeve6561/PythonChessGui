WHITE = 'white'
BLACK = 'black'
ALPHA = 'abcdefgh'


class Piece:

    def __init__(self, name, color, pos, board):
        self.name = name
        self.color = color
        self.opponent = WHITE * (self.color == BLACK) + \
            BLACK * (self.color == WHITE)
        self.position = pos
        self.rank = 7 - pos[1]
        self.file = ALPHA[pos[0]]
        self.board = board
        self.moved = False

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return self.name.capitalize() + '(' + self.color + ', ' + self.file + str(self.rank) + ', ' + str(self.moved) + ')'

    def get_attacking_squares(self):
        return []

    def get_possible_moves(self):
        return []


class Pawn(Piece):

    def __init__(self, color, pos, board):
        super().__init__('pawn', color, pos, board)

    def get_attacking_squares(self):
        attacking_squares = []

        if self.color == WHITE:
            left = (self.position[0] - 1, self.position[1] - 1)
            right = (self.position[0] + 1, self.position[1] - 1)
        elif self.color == BLACK:
            left = (self.position[0] - 1, self.position[1] + 1)
            right = (self.position[0] + 1, self.position[1] + 1)
            
        if self.board.is_on_board(left):
            attacking_squares.append(left)
            
        if self.board.is_on_board(right):
            attacking_squares.append(right)

        return attacking_squares

    def get_possible_moves(self):
        return []


class Rook(Piece):

    def __init__(self, color, pos, board):
        super().__init__('rook', color, pos, board)

    def get_attacking_squares(self):
        return []

    def get_possible_moves(self):
        return []


class Bishop(Piece):

    def __init__(self, color, pos, board):
        super().__init__('bishop', color, pos, board)

    def get_attacking_squares(self):
        return []

    def get_possible_moves(self):
        return []


class Knight(Piece):

    def __init__(self, color, pos, board):
        super().__init__('knight', color, pos, board)

    def get_attacking_squares(self):
        return []

    def get_possible_moves(self):
        return []


class Queen(Piece):

    def __init__(self, color, pos, board):
        super().__init__('queen', color, pos, board)

    def get_attacking_squares(self):
        return []

    def get_possible_moves(self):
        return []


class King(Piece):

    def __init__(self, color, pos, board):
        super().__init__('king', color, pos, board)

    def get_attacking_squares(self):
        return []

    def get_possible_moves(self):
        return []


if __name__ == '__main__':
    # pawn = Piece('pawn', WHITE, (0,1), None)
    # print(pawn.opponent)
    pass
