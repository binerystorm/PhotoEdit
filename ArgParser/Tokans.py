import enum

class Tokans(enum.Enum):
  EOF = -1
  STR = 0
  NUM = 1
  FLAG = 2
  FUNC = 3

class Tokan:
  def __init__(self, t, v):
    self.TYPE = t
    self.VAL = v

  def __str__(self):
    return "Type: {}, Value: {}".format(self.TYPE, self.VAL)
