# TODO: add type hinting

# imports

import re
# TODO: make a testing git branch where I can test all modules sepratly
if __name__ == "__main__":
  from TokanClass import Tokans, Tokan
else:
  from .TokanClass import Tokans, Tokan


class Lexer:
  # TODO: remove these lists
  flags = ["-f"]
  funcs = ["open"]
  def __init__(self):
    # Public vars
    tokan_stream = None
    char_stream = None

    # Private vars
    self.rflag = re.compile("-[a-z,A-Z]+")
    self.rfunc = re.compile("[a-z,A-Z]+")
    self.rnum = re.compile("\d+")
    self.rstr = re.compile("\".+\"")

  # Public methods
  # TODO: turn this function into generator function
  def gen_tokan_stream(self, cs):
    self.char_stream = cs
    self.tokan_stream = []

    # debugger
    # print(self.char_stream.split())

    for sub_string in self.char_stream.split():
      self.tokan_stream.append(self._gen_tokan(sub_string))
    
    return self.tokan_stream

  # Private methods
  def _gen_tokan(self, tok):
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

def main():
  pass

def test():
  l = Lexer()

  s = input("> ")
  ts = l.gen_tokan_stream(s)
  for i in ts:
    print(i)

if __name__ == "__main__":
  test()
