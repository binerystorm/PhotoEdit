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
    self.current_tok = None
    self.FLAGS = {"open": ("-f", "-o")}
    self.ARGS = {"-f": (str),
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
      tok = next(self.tokan_stream)
    except StopIteration:
      tok = Tokan(Tokans.EOF, None)

    self.current_tok = tok

  def _parse_exp(self):
    # vars def
    self._popt()
    func = self.current_tok

    # logic
    if func.VAL not in self.FLAGS.keys():
      try:
        raise Exception("unknown function")
      except Exception as e:
        return "Exception: {}".format(e)

    if func.TYPE == Tokans.FUNC:
      return self._parse_func(func)
    else:
      raise Exception("Expected type FUNC, got type {}".format(func.TYPE))
    
  def _parse_func(self, func):
    # var def
    flag_list = []
    self._popt()

    # logic
    while self.current_tok.TYPE == Tokans.FLAG:

      if self.current_tok.VAL in self.FLAGS[func.VAL]:
        flag = self.current_tok
        flag_list.append(self._parse_flag(flag))

      else:
        raise Exception("Flag not compatible with func")
    # end while

    if self.current_tok.TYPE == Tokans.EOF:
      if flag_list == []:
        return CmdNode(func, [None])

      else:
        return CmdNode(func, flag_list)

    else: 
      raise Exception("expected flag after functions")

  def _parse_flag(self, flag):
    # var def
    arg_list = []
    self._popt()

    # logic
    while self.current_tok.TYPE in (Tokans.NUM, Tokans.STR):
      if type(self.current_tok.VAL) == self.ARGS[flag.VAL]:
        arg_list.append(ArgNode(self.current_tok))
      else:
        raise Exception("incorrect type for flag")
      self._popt()
      

    if arg_list == []:
      return FlagNode(flag, [None])
    else:
      return FlagNode(flag, arg_list)

# end class


if __name__ == "__main__":
  arg = "open -f \"hallo\"" # test an expretion
  arg2 = "open -o" # test another valid expretion
  arg3 = "open -f \"hallo\" -o" # test an expretion with more than one flag
  arg4 = "open -o -f \"hallo\"" # test an expretion with more than one flag in another order
  arg5 = "open" # test expretion with no flags
  arg6 = "bla" # test expretion with invalid funtion
  p = ArgParser()
  print(p.parse(arg))
  print(p.parse(arg2))
  print(p.parse(arg3))
  print(p.parse(arg4))
  print(p.parse(arg5))
  print(p.parse(arg6))


