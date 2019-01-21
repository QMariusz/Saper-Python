from AbstractAssetManeger import AbstractAssetManeger
from tkinter import *

class FieldAsset(AbstractAssetManeger):

    def __init__(self):
        self.loadAssets()

    def loadAssets(self):
        self._assets = {key : PhotoImage(file="graphics/" + str(key) + ".png") for key in range(0, 9)}

    def getAssets(self):
        return self._assets