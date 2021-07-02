from Math import Tokans, Tokan, Lexer, AddNode, NumberNode, SubNode, DevNode, MultNode

class Parser2:
  
  def __init__(self, tokan_stream):
    self.tokan_stream = tokan_stream
    self.index = 0

  def _raise_exception(self, next_tok):
    if next_tok.TYPE != Tokans.NUM:
      Exception("fubction canot follow function")
    

  def _at_eof(self):
    return self.index >= len(self.tokan_stream)

  def _peekt(self):
    if not self._at_eof():
      return self.tokan_stream[self.index]
    else:
      return Tokan(None, Tokans.EOF)

  def _popt(self):
    tok = self._peekt()
    self.index += 1
    return tok

  def parse_factor(self, tok):
    return NumberNode(tok)

  def parse_term(self, current_tok):

    # should only run if current tokan is a number
    root_node = False
    left_node = NumberNode(current_tok)
    
    # if the current tokan is not one of these tokans then we can exit this function
    while current_tok.TYPE in (Tokans.MULT, Tokans.DEV, Tokans.NUM):
      print(self.index)
      next_tok = self._peekt()

      # if tokan is a number 
      if current_tok.TYPE == Tokans.NUM:
        right_node = NumberNode(current_tok)

        # create new left node
        if root_node and root_node.TYPE == Tokans.MULT:
          left_node = MultNode(left_node, right_node)
        elif root_node and root_node.TYPE == Tokans.DEV:
          left_node = DevNode(left_node, right_node)

      # if the current tokan is a operater of type term
      elif current_tok.TYPE == Tokans.MULT:
        root_node == current_tok                                          # save the tokan for when we get the right side of the term
        self._raise_exception(next_tok)                                   # check for incorrect term
      elif current_tok.TYPE == Tokans.MULT:
        root_node == current_tok                                          # save the tokan for when we get the right side of the term
        self._raise_exception(next_tok)                                   # check for incorrect term

      current_tok = self._popt()                                          # get next tokan

    return left_node


  def parse_exp(self):
    # set up
    current_tok = self._popt()
    root_node = False

    # should only run if current tokan is a number
    left_node = self.parse_term(current_tok)
    
    # if the current tokan is not an eof continue
    while current_tok.TYPE != Tokans.EOF:
      print(self.index)
      print(self._at_eof())
      print(current_tok)
      next_tok = self._peekt()

      # if tokan is a number 
      if current_tok.TYPE == Tokans.NUM:
        right_node = self.parse_term(current_tok)

        # create new left node
        if root_node and root_node.TYPE == Tokans.ADD:
          left_node = AddNode(left_node, right_node)
        elif root_node and root_node.TYPE == Tokans.SUB:
          left_node = SubNode(left_node, right_node)

      # if the current tokan is a operater of type term
      elif current_tok.TYPE == Tokans.ADD:
        root_node == current_tok                                          # save the tokan for when we get the right side of the term
        self._raise_exception(next_tok)                                   # check for incorrect term
      elif current_tok.TYPE == Tokans.SUB:
        root_node == current_tok                                          # save the tokan for when we get the right side of the term
        self._raise_exception(next_tok)                                   # check for incorrect term

      current_tok = self._popt()                                          # get next tokan

    return left_node
    # TODO: add parse_expre

string = "1 + 2"
l = Lexer(string)
tok_s = l.gen_tokan_stream()
p = Parser2(tok_s)
e = p.parse_exp()
print(e)
