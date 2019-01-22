import unittest
from Game import Game
from tkinter import *
from FileController import FileController
import time
from field import Field
from asset.SpecAsset import SpecAsset
from asset.FieldAsset import FieldAsset
from exception.WrongDataException import WrongDataException

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

    def test_loadSpecAsset(self):
        stage= Tk()
        specAsset = SpecAsset()

        self.assertIsInstance(specAsset.getAssets()[1], PhotoImage)

    def test_loadFieldAsset(self):
        stage= Tk()
        fieldAsset = FieldAsset()

        self.assertIsInstance(fieldAsset.getAssets()[1], PhotoImage)

    def test_gameResetWithWrongParameters(self):
        stage = Tk()
        game = Game(stage, 0, 0, 0)

        with self.assertRaises(WrongDataException):
            game.reset(16,16,14)

    def test_gameResetWithWrongParameters2(self):
        stage = Tk()
        game = Game(stage, 0, 0, 0)

        with self.assertRaises(ValueError):
            game.reset('a','b','c')

    def test_loadScore(self):
        stage = Tk()
        fileController = FileController(stage)

        fileController.loadScore()
        self.assertEqual(fileController.rekordy[0][0], 'Rekordy poziom Łatwy')

    def test_fieldTypeAfterRightClickOnFreeField(self):
        stage = Tk()
        game = Game(stage, 4, 4, 0)
        game._flags = 1
        game.rightClick(0)

        self.assertEqual(game._buttons[0].getTyp(), 'flag')

    def test_fieldTypeAfterRightClickOnFlagedField(self):
        stage = Tk()
        game = Game(stage, 4, 4, 0)
        game._buttons[0].setTyp("flag")
        game.rightClick(0)

        self.assertEqual(game._buttons[0].getTyp(), 'question')

    def test_fieldTypeAfterRightClickOnQuestionedField(self):
        stage = Tk()
        game = Game(stage, 4, 4, 0)
        game._buttons[0].setTyp("question")
        game.rightClick(0)

        self.assertEqual(game._buttons[0].getTyp(), 'free')

    def test_lostStateAfterLeftClickOnBomb(self):
        stage = Tk()
        game = Game(stage, 4, 4, 0)
        game._buttons[0].setBomb()
        game.leftClick(0)

        self.assertEqual(game._state, 'lost')

if __name__ == '__main__':
    unittest.main()