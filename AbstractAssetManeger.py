from abc import ABC, abstractmethod

class AbstractAssetManeger(ABC):

    def __init__(self):
        self._assets = {}

    @abstractmethod
    def loadAssets(self):
        pass

    @abstractmethod
    def getAssets(self):
        pass