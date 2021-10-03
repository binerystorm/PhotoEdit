import set_up
import pytest
import unittest

from ArgParser.TokanClass import Tokan, Tokans
from ArgParser.LexerClass import Lexer

class TestLexer(unittest.TestCase):
  def test_gen_tokan(self):
    l = Lexer()
    self.assertEqual(l._gen_tokan("\"hallo\""), Tokan(Tokans.STR, "hallo"))
