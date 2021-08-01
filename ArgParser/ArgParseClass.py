from Tokans import Tokans, Tokan
from LexerClass import Lexer
from Nodes import FlagNode, ArgNode, CmdNode

class ArgParser:
  def __init__(self):
    # Public vars
    self.arg = None

    # Private vars
    self.lex = Lexer()
    self.tokan_stream = None
    self.FUNCS = {"open": ("-f", "-o")}
    self.FLAGS = {"-f": (str),
                  "-o": (int, None)}

  # Public methods
  def parse(self, arg):
    self.arg = self.lex.gen_tokan_stream(arg)
    self.tokan_stream = iter(self.arg)
    root = self._parse_exp()
    return root

  # Private methods
  def _popt(self):
    try:
      ret = next(self.tokan_stream)
    except StopIteration:
      ret = Tokan(Tokans.EOF, None)
    return ret

  def _parse_exp(self):
    func = self._popt()
    if func.TYPE == Tokans.FUNC:
      return self._parse_func(func)
    else:
      raise Exception("Expected type FUNC, got type {}".format(func.TYPE))
    
  def _parse_func(self, func):
    # var def
    flag_list = []
    next_tok = self._popt()

    # logic
    while next_tok.TYPE == Tokans.FLAG:
      print("test: ", next_tok.VAL)
      if next_tok.VAL in self.FUNCS[func.VAL]:
        flag_list.append(self._parse_flag(next_tok))
      else:
        raise Exception("Flag not compatible with func")
      
      if next_tokan.TYPE == Tokans.FLAG:
        continue
      else:
        next_tok = self._popt()

    if next_tok.TYPE == Tokans.EOF:
      return CmdNode(func, flag_list)
    else:
      raise Exception("expected flag after functions")

  def _parse_flag(self, flag):
    arg_list = []
    next_tok = self._popt()

    while next_tok.TYPE in (Tokans.NUM, Tokans.STR):
      if type(next_tok.VAL) in self.FLAGS[flag]:
        arg_list.append(ArgNode(next_tok))
      else:
        raise Exception("incorrect type for flag")
      next_tok = self._popt()

    if next_tok.TYPE in (Tokans.EOF, Tokans.FLAG):
      return FlagNode(flag, arg_list)
    else:
      raise Exception("expected flag or arg got {}".format(next_tok.TYPE))


if __name__ == "__main__":
  arg = ""
  p = ArgParser()
  while arg != "quit":
    arg = input("> ")
    print(p.parse(arg))

