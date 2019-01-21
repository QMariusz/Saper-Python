from tkinter import *
from Game import Game

class Application(object):

    if __name__ == "__main__":
        stage = Tk()
        stage.title("Saper")
        game = Game(stage, 0, 0, 0)
        stage.mainloop()