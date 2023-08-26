from tkinter import *
from PIL import ImageTk, Image
import os

LIGHT_SQUARE = '#e7c7fc'
DARK_SQUARE = '#2d0547'
SQUARE_SIZE = 80

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

        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.board[(j, i)] = ChessTile(self, LIGHT_SQUARE, (j, i))
                else:
                    self.board[(j, i)] = ChessTile(self, DARK_SQUARE, (j, i))


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