import enum

class Tokans(enum.Enum)
  ARG = 0
  FLAG = 0
  FUNC = 0
  EOF = 0

class Tokan:
  def __init__(self, t, v):
    self.TYPE = t
    self.VAL = v
