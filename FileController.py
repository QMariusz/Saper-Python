import time
from tkinter import *

class FileController(object):

    def __init__(self, stage):
        self.loadScore()
        self._stage = stage

    def loadScore(self):
        self.rekordy = [[0 for x in range(4)] for y in range(3)]
        i=0
        j=1

        self.rekordy[0][0] = 'Rekordy poziom Łatwy'
        self.rekordy[1][0] = 'Rekordy poziom Średni'
        self.rekordy[2][0] = 'Rekordy poziom Trudny'
        with open("config.txt", 'r') as f:
            for line in f:
                line = line.strip()
                self.rekordy[i][j] = line
                j+=1
                if j==4:
                    i+=1
                    j=1

    def showRecords(self):
        filewin = Toplevel(self._stage)
        for i in range(3):
            for j in range(4):
                labelW = Label(filewin, text=self.rekordy[i][j])
                labelW.grid(row=j + 1 + i * 4, column=1)

    def saveScore(self):
        with open("config.txt", 'w') as f:
            for i in range(3):
                for j in range(3):
                    f.write(str(self.rekordy[i][j+1])+ '\n')

    def checkRecord(self,w,h,b,i, width, height, bombs, czas):
        if width == w and height == h and bombs == b:
            a = round(time.time() - czas, 1)
            if a < float(self.rekordy[i][1]) or self.rekordy[i][1] == '0':
                self.rekordy[i][3] = self.rekordy[i][2]
                self.rekordy[i][2] = self.rekordy[i][1]
                self.rekordy[i][1] = a
            elif a < float(self.rekordy[i][2]) or self.rekordy[i][2] == '0':
                self.rekordy[i][3] = self.rekordy[i][2]
                self.rekordy[i][2] = a
            elif a < float(self.rekordy[i][3]) or self.rekordy[i][3] == '0':
                self.rekordy[i][3] = a
