# imports
from typing import Union, Optional, Iterator
from .TokanClass import Tokans, Tokan
from .LexerClass import Lexer
from .Nodes import FlagNode, ArgNode, CmdNode

# TODO: add type hinting

# TODO: make a testing git branch where I can test all modules sepratly

class ArgParser:
  def __init__(self) -> None:
    # Public vars
    self.arg: Optional[list[Tokan]] = None

    # Private vars
    self.lex: Lexer = Lexer()
    self.tokan_stream: Iterator[Tokan]
    self.current_tok: Tokan
    # TODO: add assets(data) folder in project, add self.FLAGS, self.ARGS to mensioned folder
    self.FLAGS: dict[str, tuple[str, ...]] = {
        "open": ("-f", "-o"),
        "echo": ("-v", "-eq")}
    self.ARGS: dict[str, tuple[str, ...]] = {
        # TODO: fix arguement system, each funtion must have its own flags
        "-f": (str,),
        "-o": (int, None),
        "-v": (str, None),
        "-eq": (str, float, int)}

  # TODO: add error handeler
  # TODO: refacter this code at some point (not essentail)
  # Public methods
  def parse(self, arg: str) -> CmdNode:
    # TODO: make this accept genorator function
    self.arg = self.lex.gen_tokan_stream(arg)
    self.tokan_stream = iter(self.arg)
    root: CmdNode = self._parse_exp()
    return root

  # Private methods
  def _popt(self) -> None:
    tok: Tokan
  
    try:
      tok = next(self.tokan_stream)
    except StopIteration:
      tok = Tokan(Tokans.EOF, None)

    self.current_tok = tok

  def _parse_exp(self) -> CmdNode:
    func: Tokan
    # vars def
    self._popt()
    func = self.current_tok

    # logic
    if func.VAL not in self.FLAGS.keys():
      raise Exception("unknown function")

    if func.TYPE == Tokans.FUNC:
      return self._parse_func(func)
    else:
      raise Exception("Expected type FUNC, got type {}".format(func.TYPE))
    
  def _parse_func(self, func: Tokan) -> CmdNode:
    # var def
    flag: Tokan
    flag_list: list[FlagNode] = []
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

  def _parse_flag(self, flag: Tokan) -> FlagNode:
    # var def
    arg_list: list[ArgNode] = []
    self._popt()

    # logic
    while self.current_tok.TYPE in (Tokans.NUM, Tokans.STR):
      if type(self.current_tok.VAL) in self.ARGS[flag.VAL]:
        arg_list.append(ArgNode(self.current_tok))
      else:
        raise Exception("incorrect type for flag")
      self._popt()
      

    if arg_list == []:
      return FlagNode(flag, [None])
    else:
      return FlagNode(flag, arg_list)


# TODO: fix test function (its a mess)
def test() -> None:
  arg: str = "open -f \"hallo\"" # test an expretion
  arg2: str = "open -o" # test another valid expretion
  arg3: str = "open -f \"hallo\" -o" # test an expretion with more than one flag
  arg4: str = "open -o -f \"hallo\"" # test an expretion with more than one flag in another order
  arg5: str = "open" # test expretion with no flags
  arg6: str = "echo -eq 1 2"
  arg7: str = "bla" # test expretion with invalid funtion
  p: ArgParser = ArgParser()
  # print(p.parse(arg))
  # print(p.parse(arg2))
  # print(p.parse(arg3))
  # print(p.parse(arg4))
  # print(p.parse(arg5))
  print(p.parse(arg6))
  # print(p.parse(arg7))

def main() -> None:
  pass

if __name__ == "__main__":
  test()


