from pieces import *
from board import *
from tkinter import *
import os
from PIL import ImageTk, Image


TITLE = '2-Player Chess by Jeeve'
PATH = os.path.dirname(os.path.realpath(__file__))


def main():
    global PATH, TITLE
    
    root = Tk()
    root.resizable(False, False)
    root.title(TITLE)
    root.iconbitmap(PATH + '/images/icon.ico')
    
    img = ImageTk.PhotoImage(Image.open(PATH+'/images/chess.png'))
    picture = Label(root, bg='blue', image=img)
    picture.grid(row=0, column=0, rowspan=2)

    start = Button(root, bg='green', text='Start Game', padx=113,
                   pady=100, font=('Arial', 20), command=Board)
    start.grid(row=0, column=1)

    end = Button(root, bg='red', text='Exit Game', padx=120,
                 pady=100, font=('Arial', 20), command=root.quit)
    end.grid(row=1, column=1)
    
    root.mainloop()



if __name__ == '__main__':
    main()
    pass