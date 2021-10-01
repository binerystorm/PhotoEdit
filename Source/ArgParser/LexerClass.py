# TODO: add type hinting

# imports

import typing
import re
# TODO: make a testing git branch where I can test all modules sepratly
# if __name__ == "__main__":
#   pass
#   # from TokanClass import Tokans, Tokan
# else:
from .TokanClass import Tokans, Tokan


class Lexer:
  # TODO: remove these lists
  flags = ["-f"]
  funcs = ["open"]
  def __init__(self) -> None:
    # Public vars
    self.tokan_stream: list[Tokan] = []
    self.char_stream: str = ""

    # Private vars
    self.rflag: re.Pattern = re.compile("-[a-z,A-Z]+")
    self.rfunc: re.Pattern = re.compile("[a-z,A-Z]+")
    self.rnum: re.Pattern = re.compile("\d+")
    self.rstr: re.Pattern = re.compile("\".+\"")

  # Public methods
  # TODO: turn this function into generator function
  def gen_tokan_stream(self, cs: str) -> list[Tokan]:
    self.char_stream = cs

    # debugger
    # print(self.char_stream.split())

    for sub_string in self.char_stream.split():
      self.tokan_stream.append(self._gen_tokan(sub_string))
    
    return self.tokan_stream

  # Private methods
  def _gen_tokan(self, tok: str) -> Tokan:
    if self.rflag.fullmatch(tok):
      return Tokan(Tokans.FLAG, tok)
    elif self.rfunc.fullmatch(tok):
      return Tokan(Tokans.FUNC, tok)
    elif self.rstr.fullmatch(tok):
      return Tokan(Tokans.STR, tok.strip('"'))
    elif self.rnum.fullmatch(tok):
      return Tokan(Tokans.NUM, tok)
    else:
      raise Exception("pattern not recognised")

def main() -> None:
  pass

def test() -> None:
  l: Lexer = Lexer()

  s:str = input("> ")
  ts:list[Tokan] = l.gen_tokan_stream(s)
  for i in ts:
    print(i)

if __name__ == "__main__":
  test()
