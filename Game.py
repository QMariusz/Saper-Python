# coding=utf-8
import sys
import random
from tkinter import *
import Error
from Klasy import *
import time
from field import Field
from FieldAsset import FieldAsset
from SpecAsset import SpecAsset
from FileController import FileController


class Game(object):

    def __init__(self, stage, width, height, bombs):
        self._fieldAsset = FieldAsset()

        self._specAsset = SpecAsset()

        self._fields = self._fieldAsset.getAssets()
        self._special = self._specAsset.getAssets()

        self._fileController = FileController(stage)
        self._flags = bombs
        self._stage = stage
        self._czas = time.time()
        self._bombs = bombs
        self._width = width
        self._height = height

        self._count = 0
        self._elements = width * height
        self._count = width * height
        self._bottomFrame = Frame(stage)
        self._state = 'game'
        self.createMenu()

        self.createButton(stage)
        self.createBombs()

        self.createMenuBar()

    def createMenu(self):
        self._bottomFrame.grid(row=1, columnspan=80)

        self._buttonFrame = Frame(self._stage)
        self._buttonFrame.grid(row=self._height + 100, columnspan=80)

        self._label = Label(self._buttonFrame, text="")
        self._label.grid(row=1, column=1)

        self._flagRemainning = Label(self._buttonFrame, text='Flags left: ' + str(self._flags))
        self._flagRemainning.grid(row=1, column=2)

        self._quitBtn = Button(self._buttonFrame, text='Quit', command=self.quit)
        self._quitBtn.grid(row=1, column=3)

        self._labelW = Label(self._bottomFrame, text='W: ')
        self._labelW.grid(row=1, column=1)

        self._entryWidth = Entry(self._bottomFrame)
        self._entryWidth.grid(row=1, column=2)

        self._labelH = Label(self._bottomFrame, text='H: ')
        self._labelH.grid(row=2, column=1)

        self._entryHeight = Entry(self._bottomFrame)
        self._entryHeight.grid(row=2, column=2)

        self._entryBomb = Entry(self._bottomFrame)
        self._entryBomb.grid(row=3, column=2)

        self._labelB = Label(self._bottomFrame, text='B: ')
        self._labelB.grid(row=3, column=1)

        self._applyBtn = Button(self._bottomFrame, text='Play', command=self.play)
        self._applyBtn.grid(row=4, column=2)

        self._resetBtn = Button(self._buttonFrame, text='Reset', command=self.resetButton)
        self._resetBtn.grid(row=1, column=4)

        self._labelError = Label(self._buttonFrame, text="", fg="red")

    def createMenuBar(self):
        self._stage.bind('<KeyPress-x><KeyPress-y><KeyPress-z><KeyPress-z><KeyPress-y>', self.showMines)

        menubar = Menu(self._stage)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Łatwy", command=lambda: self.reset(8, 8, 1))
        filemenu.add_command(label="Średni", command=lambda: self.reset(10, 10, 14))
        filemenu.add_command(label="Trudny", command=lambda: self.reset(14, 14, 30))
        filemenu.add_separator()
        filemenu.add_command(label="Rekordy", command=self._fileController.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self._stage.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self._stage.config(menu=menubar)

    def showInformationLabel(self, text):
        filewin = Toplevel(self._stage)
        labelW = Label(filewin, text=text)
        labelW.grid(row=1, column=1)

    def showMines(self, event):
        for i in range(self._elements):
            if self._buttons[i].getBomb():
                self._buttons[i].config(image=self._special[11])

    def createButton(self, stage):

        self._buttons = []
        r = 1
        c = 1
        for x in range(0, self._elements):

            self._buttons.append(Field('free', self._buttonFrame, r, c, height=20, width=20, image=self._special[3]))

            self._buttons[x].grid(row=r + 1, column=c + 1)

            self._buttons[x].bind('<Button-1>', self.leftClick_w(x))
            self._buttons[x].bind('<Button-3>', self.rightClick_w(x))

            c += 1
            if c == self._width + 1:
                c = 1
                r += 1

    def update_clock(self):
        now = time.time()
        self._label.configure(text=round(now - self._czas, 1))
        if self._state == 'game':
            self._stage.after(100, self.update_clock)

    def createBombs(self):
        i = 0
        while i < self._flags:
            a = random.randint(0, self._elements - 1)
            if not self._buttons[a].getBomb():
                self._buttons[a].setBomb()
                i += 1
                if self._buttons[a].getRow() > 1:
                    self._buttons[a - self._width].setValue()
                    if self._buttons[a].getCol() > 1:
                        self._buttons[a - self._width - 1].setValue()
                    if self._buttons[a].getCol() < self._width:
                        self._buttons[a - self._width + 1].setValue()
                if self._buttons[a].getRow() < self._height:
                    self._buttons[a + self._width].setValue()
                    if self._buttons[a].getCol() > 1:
                        self._buttons[a + self._width - 1].setValue()
                    if self._buttons[a].getCol() < self._width:
                        self._buttons[a + self._width + 1].setValue()
                if self._buttons[a].getCol() > 1:
                    self._buttons[a - 1].setValue()
                if self._buttons[a].getCol() < self._width:
                    self._buttons[a + 1].setValue()

    def reset(self, c, d, bombs):
        c = int(c)
        d = int(d)
        bombs = int(bombs)

        if not 2 <= c <= 15 or not 2 <= d <= 15 or not 0 <= bombs <= c * d:
            raise Error.WrongDataException("")

        for i in range(0, self._elements):
            self._buttons[i].destroy()
        self._buttons.clear()
        self._flags = bombs
        self._labelError.grid_forget()
        self._flagRemainning.config(text='Flags left : ' + str(self._flags))
        self._count = c * d
        self._width = c
        self._height = d
        self._bombs = bombs
        self._elements = c * d
        self.createButton(self._stage)
        for i in range(0, self._elements):
            self._buttons[i].config(image=self._special[3], text='', state='normal', relief=RAISED)

        [y.reset() for y in self._buttons]
        self.createBombs()
        self._state = 'game'
        self._czas = time.time()
        self.update_clock()

    def play(self):
        c = self._entryWidth.get()
        d = self._entryHeight.get()
        bombs = self._entryBomb.get()
        try:
            self.reset(c, d, bombs)
        except ValueError:
            self._labelError.grid(row=2, columnspan=5)
            self._labelError.config(text="Niepoprawne dane")
        except Error.WrongDataException:
            self._labelError.grid(row=2, columnspan=5)
            self._labelError.config(text="Zla wielkosc pola lub zla lizcba bomb")

        self._state = 'game'
        self._czas = time.time()

    def quit(self):
        self._fileController.saveScore()
        self._stage.destroy()

    def leftClick_w(self, x):
        return lambda Button: self.leftClick(x)

    def rightClick_w(self, x):
        return lambda Button: self.rightClick(x)

    def leftClick(self, btn):
        if self._state != 'won':
            if self._buttons[btn].getBomb() == True and self._buttons[btn].getTyp() != 'end':
                self._buttons[btn].config(image=self._special[9])
                self.lost()

            elif self._buttons[btn].getTyp() == 'free':
                self._buttons[btn].config(image=self._fields[self._buttons[btn].getValue()])
                self._count -= 1
                self._buttons[btn].setTyp('value')
                if self._buttons[btn].getValue() == 0:
                    self.showSafe(btn)
                self.checkWin()

    def rightClick(self, btn):
        if self._state != 'won':
            if self._buttons[btn].getTyp() == 'free':
                if self._flags > 0:
                    self._buttons[btn].config(image=self._special[1])
                    self._flags -= 1
                    self._count -= 1
                    self._flagRemainning.config(text='Flags Flags left : ' + str(self._flags))
                    self._buttons[btn].setTyp('flag')
                    self._buttons[btn].setShown(False)
                else:
                    self._labelError.grid(row=2, columnspan=5)
                    self._labelError.config(text="Brak flag")
            elif self._buttons[btn].getTyp() == 'flag':
                self._buttons[btn].config(image=self._special[10])
                self._buttons[btn].setTyp('question')
                self._flags += 1
                self._count += 1
                self._flagRemainning.config(text='Flags Flags left : ' + str(self._flags))
                self.checkWin()
                self._labelError.grid_forget()
            elif self._buttons[btn].getTyp() == 'question':
                self._buttons[btn].config(image=self._special[3])
                self._buttons[btn].setTyp('free')
                self._buttons[btn].setShown(True)

    def showSafe(self, x):
        if self._buttons[x].getRow() > 1:
            self.leftClick(x - self._width)
            if self._buttons[x].getCol() > 1:
                self.leftClick(x - (self._width + 1))
            if self._buttons[x].getCol() < self._width:
                self.leftClick(x - (self._width - 1))
        if self._buttons[x].getRow() < self._height:
            self.leftClick(x + self._width)
            if self._buttons[x].getCol() > 1:
                self.leftClick(x + self._width - 1)
            if self._buttons[x].getCol() < self._width:
                self.leftClick(x + self._width + 1)
        if self._buttons[x].getCol() > 1:
            self.leftClick(x - 1)
        if self._buttons[x].getCol() < self._width:
            self.leftClick(x + 1)

    def checkWin(self):
        if self._flags == self._count or self._count == 0:
            self._labelError.grid(row=2, columnspan=5)
            self._labelError.config(text="Wygrales", fg="green")
            self._state = "won"
            self._fileController.checkRecord(8, 8, 1, 0, self._width, self._height, self._bombs, self._czas)
            self._fileController.checkRecord(10, 10, 14, 1, self._width, self._height, self._bombs, self._czas)
            self._fileController.checkRecord(14, 14, 30, 2, self._width, self._height, self._bombs, self._czas)

    def lost(self):
        for i in range(self._elements):
            if self._buttons[i].getBomb():
                self._buttons[i].config(image=self._special[9])
            self._buttons[i].setTyp('end');
        self._labelError.grid(row=2, columnspan=5)
        self._labelError.config(text="Przegrales", fg="red")
        self._state = 'lost'

    def resetButton(self):
        try:
            self.reset(self._width, self._height, self._bombs)
        except ValueError:
            self.showInformationLabel("Niepoprawne dane")
        except Error.WrongDataException:
            self.showInformationLabel("Zla wielkosc pola lub zla lizcba bomb")
