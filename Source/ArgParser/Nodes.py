from typing import Optional, Sequence
from .TokanClass import Tokan, Tokans
# TODO: add type hinting

# TODO: add Node classes to assets(data) module

class ArgNode:
  def __init__(self, tokan: Tokan) -> None:
    self.val: Optional[str] = tokan.VAL

  def __repr__(self) -> str:
    return "{}".format(self.val)

  def __str__(self) -> str:
    return str(self.val)


class FlagNode:
  def __init__(self, tokan: Tokan, arguments: list[Optional[ArgNode]]):
    self.val: Optional[str] = tokan.VAL
    self.args: list[Optional[ArgNode]] = arguments

  def __repr__(self) -> str:
    ret: str = "Val: {} <".format(self.val)
    for i in self.args:
      ret += "{}".format(i)
      ret += ", "
    ret += ">, "
    return ret


class CmdNode:
  def __init__(self, tokan: Tokan, arguments: list[Optional[FlagNode]]) -> None:
    self.val: Optional[str] = tokan.VAL
    self.args: list[Optional[FlagNode]] = arguments

  def __repr__(self) -> str:
    ret: str = "Val: {} <".format(self.val)
    for i in self.args:
      ret += "{}".format(i)
    ret += ">"
    return ret

# TODO: Remove this crap (this doesn't need to be tested)
if __name__ == "__main__":
  from .LexerClass import Lexer
  l: Lexer = Lexer()
  cmd: Tokan
  flag: Tokan
  arg: Tokan
  cmd, flag, arg = l.gen_tokan_stream("open -f \"/home\"") 
  argn: ArgNode = ArgNode(arg)
  argl: list[Optional[ArgNode]] = [argn]
  flagn: FlagNode = FlagNode(flag, argl)
  flagl: list[Optional[FlagNode]] = [flagn]
  cmdn: CmdNode = CmdNode(cmd, flagl)
  print(cmd)

