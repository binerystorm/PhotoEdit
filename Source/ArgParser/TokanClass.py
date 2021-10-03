from typing import Optional
import enum

class Tokans(enum.Enum):
  EOF = -1
  STR = 0
  NUM = 1
  FLAG = 2
  FUNC = 3

class Tokan:
  def __init__(self, t: Tokans, v: Optional[str]) -> None:
    self.TYPE: Tokans = t
    self.VAL: Optional[str] = v 

  def __str__(self) -> str:
    return "Type: {}, Value: {}".format(self.TYPE, self.VAL)

  def __repr__(self) -> str:
    return "Type: {}, Value: {}".format(self.TYPE, self.VAL)

  def __eq__(self, other) -> bool:
    return isinstance(other, Tokan) and self.VAL == other.VAL and self.TYPE == other.TYPE
