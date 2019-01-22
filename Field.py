from tkinter import *

class Field(Button):

    def __init__(self, typ, stage, row, col, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'gray'
        self._color = (0, 255, 0)
        self._typ = typ
        self._bomb = False
        self._row = row
        self._col = col
        self._value = 0
        self._shown = True

    def reset(self):
        self._value = 0
        self._typ = 'free'
        self._shown = True
        self._bomb = False

    def setShown(self, b):
        self._shown = b

    def setBomb(self):
        self._bomb = True

    def getBomb(self):
        return self._bomb

    def getShown(self):
        return self._shown

    def getTyp(self):
        return self._typ

    def setTyp(self, typ):
        self._typ = typ

    def getValue(self):
        return self._value

    def setValue(self):
        self._value += 1

    def getRow(self):
        return self._row

    def getCol(self):
        return self._col
