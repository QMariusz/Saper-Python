import unittest
from Game import Game
from tkinter import *
from FileController import FileController
import time
from field import Field
from SpecAsset import SpecAsset
from FieldAsset import FieldAsset
from Error import WrongDataException

class TestSaper(unittest.TestCase):

    def test_loseState(self):
        stage = Tk()
        game = Game(stage, 0, 0, 0)

        game.lost()
        self.assertEqual(game._state, 'lost')

    def test_checkNewRecord(self):
        stage = Tk()
        fileController = FileController(stage)

        fileController.checkRecord(2, 2, 2, 1, 2, 2, 2, time.time()-0.1)
        self.assertEqual(fileController.rekordy[1][1], 0.1)

    def test_fieldReset(self):
        stage = Tk()
        field = Field('flag', stage, 1, 1)
        field.setBomb()
        field.setShown(False)

        field.reset()
        self.assertEqual(field.getTyp(), 'free')
        self.assertFalse(field.getBomb())
        self.assertTrue(field.getShown())

if __name__ == '__main__':
    unittest.main()