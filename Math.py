# TOKANS CLASSES
# ==============

class Tokan:
  def __init__(self, val, tokan_type):
    self.val = val
    self.tokan_type = tokan_type


  def __eq__(self, other):
    return self.tokan_type == other.tokan_type


class BracketT(Tokan):
  def __init__(self, val, tokan_type):
    super().__init__(val, 'BracketT')


class DevideMultiplyT(Tokan):
  def __init__(self, val):
    super().__init__(val, 'DevideMultiplyT')

  def function(self, lft, rgt):
    if self.val == '/':
      return lft / rgt
    elif self.val == '*':
      return lft * rgt
    

class SubAddT(Tokan):
  def __init__(self, val):
    super().__init__(val, 'SubAddT')

  def function(self, lft, rgt):
    if self.val == '-':
      return lft - rgt
    elif self.val == '+':
      return lft + rgt


class NumT(Tokan):
  def __init__(self, val):
    super().__init__(val, 'NumT')



'''
class CmdT(Tokan):
  def __init__(self, cmd):
    self.type = "CmdT"
    self.val = cmd

  def gen_cmd(self, lft, rgt):
    if self.val == '+':
      return lft + rgt

    if self.val == '-':
      return lft - rgt

    if self.val == '*':
      return lft * rgt

    if self.val == '/':
      return lft / rgt
'''
    
# LEXER
# =====

class Lexer:
  def __init__(self, string):
    self.string = string

  def _gen_tokan(self, val):
    if val == '(' or val == ')':
      return BracketT(val)
    elif val == '+' or val == '-':
      return SubAddT(val)
    elif val == '*' or val == '/':
      return DevideMultiplyT(val)
    else:
      try:
        return NumT(float(val))
      except ValueError as e:
        return e


  def gen_tokan_stream(self):
    operation_types = ['(', ')', '+', '-', '*', '/']
    tokan_stream = []

    for sub_string in self.string.split():
      tokan_stream.append(self._gen_tokan(sub_string)) 
    return tokan_stream
    

# PARSER
# ======

class Parser:
  OOO = {
      'NumT': 0,
      'SubAddT': 1,
      'DevideMultiplyT': 2,
      'BracketT': 3
    }
  def __init__(self, tokan_stream):
    self.INDEX = 0
    self.tokan_stream = tokan_stream

  def popt(self):
    item = self.tokan_stream[self.INDEX]
    self.INDEX += 1
    return item

  def peekt(self):
    return self.tokan_stream[self.INDEX + 1]

  def parse(self):
    self.popt()
    
  def OOO_string(self):

    final_string = ''
    
    val1 = self.popt
    operation = self.popt
    val2 = self.popt

    while self.INDEX < len(self):
      if OOO[self.peekt.tokan_type] > OOO[operation.tokan_type]:
        val1 = val2
      else:



math = '1 + 2'
l = Lexer(math)
tl = l.gen_tokan_stream()
p = Parser(tl)
p.OOO_string()
