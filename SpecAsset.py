from AbstractAssetManeger import AbstractAssetManeger
from tkinter import *

class SpecAsset(AbstractAssetManeger):

    def __init__(self):
        self.loadAssets()

    def loadAssets(self):
        self._assets = {key : PhotoImage(file="graphics/spec" + str(key) + ".png") for key in range(1, 12)}

    def getAssets(self):
        return self._assets