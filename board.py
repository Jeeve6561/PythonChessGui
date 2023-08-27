from tkinter import *
from PIL import ImageTk, Image
import os
from pieces import *

LIGHT_SQUARE = '#e7c7fc'
DARK_SQUARE = '#2d0547'
SQUARE_SIZE = 80
WHITE = 'white'
BLACK = 'black'

PATH = os.path.dirname(os.path.realpath(__file__))
IMAGES = {}
IMAGE_NAMES = ['white/pawn', 'white/rook', 'white/bishop', 'white/knight', 'white/queen', 'white/king',
               'black/pawn', 'black/rook', 'black/bishop', 'black/knight', 'black/queen', 'black/king']


def load_images():
    global IMAGES, IMAGE_NAMES, PATH
    for name in IMAGE_NAMES:
        IMAGES[name] = ImageTk.PhotoImage(
            Image.open(PATH + '\\images\\' + name + '.png')
        )
    IMAGES['blank'] = PhotoImage()


class Board(Toplevel):

    def __init__(self):
        super().__init__()
        self.title('New Game')
        self.board = {}
        self.move = 0
        self.history = {}

        load_images()

        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.board[(j, i)] = ChessTile(self, LIGHT_SQUARE, (j, i))
                else:
                    self.board[(j, i)] = ChessTile(self, DARK_SQUARE, (j, i))
                    
        self.set_up_pieces()
                    

    def set_up_pieces(self):
        for i in range(8):
            self.board[(i, 6)].put_piece(Pawn(WHITE, (i, 6), self))
            self.board[(i, 1)].put_piece(Pawn(BLACK, (i, 1), self))

        self.board[(0, 0)].put_piece(Rook('black', (0, 0), self))
        self.board[(1, 0)].put_piece(Knight('black', (1, 0), self))
        self.board[(2, 0)].put_piece(Bishop('black', (2, 0), self))
        self.board[(3, 0)].put_piece(Queen('black', (3, 0), self))
        self.board[(4, 0)].put_piece(King('black', (4, 0), self))
        self.board[(5, 0)].put_piece(Bishop('black', (5, 0), self))
        self.board[(6, 0)].put_piece(Knight('black', (6, 0), self))
        self.board[(7, 0)].put_piece(Rook('black', (7, 0), self))

        self.board[(0, 7)].put_piece(Rook('white', (0, 7), self))
        self.board[(1, 7)].put_piece(Knight('white', (1, 7), self))
        self.board[(2, 7)].put_piece(Bishop('white', (2, 7), self))
        self.board[(3, 7)].put_piece(Queen('white', (3, 7), self))
        self.board[(4, 7)].put_piece(King('white', (4, 7), self))
        self.board[(5, 7)].put_piece(Bishop('white', (5, 7), self))
        self.board[(6, 7)].put_piece(Knight('white', (6, 7), self))
        self.board[(7, 7)].put_piece(Rook('white', (7, 7), self))

    def has_piece(self, pos):
        return self.board[pos].has_piece()

    def piece_is_color(self, color, pos):
        return self.board[pos].get_color() == color

    def is_on_board(self, pos):
        return (0 <= pos[0] <= 7) and (0 <= pos[1] <= 7)


class ChessTile(Button):

    def __init__(self, master, color, pos):
        global IMAGES
        super().__init__(
            master, image=IMAGES['blank'], width=SQUARE_SIZE, height=SQUARE_SIZE, bg=color
        )
        self.color = color
        self.piece = None
        self.board = master
        self.position = pos
        self.grid(row=pos[1], column=pos[0])

    def put_piece(self, piece):
        global IMAGES
        image = IMAGES[piece.color + '/' + piece.name]
        self.config(image=image)
        self.piece = piece

    def has_piece(self):
        return self.piece != None

    def get_color(self):
        if self.piece != None:
            return self.piece.color
        return None
