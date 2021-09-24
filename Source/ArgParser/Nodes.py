
class ArgNode:
  def __init__(self, tokan):
    self.val = tokan.VAL

  def __repr__(self):
    return "{}".format(self.val)


class FlagNode:
  def __init__(self, tokan, arguments):
    self.val = tokan.VAL
    self.args = arguments

  def __repr__(self):
    ret = "Val: {} <".format(self.val)
    for i in self.args:
      ret += "{}".format(i)
      ret += ", "
    ret += ">, "
    return ret


class CmdNode:
  def __init__(self, tokan, arguments):
    self.val = tokan.VAL
    self.args = arguments

  def __repr__(self):
    ret = "Val: {} <".format(self.val)
    for i in self.args:
      ret += "{}".format(i)
    ret += ">"
    return ret

if __name__ == "__main__":
  from LexerClass import Lexer
  l = Lexer()
  cmd, flag, arg = l.gen_tokan_stream("open -f \"/home\"")
  arg = ArgNode(arg)
  arg = [arg]
  flag = FlagNode(flag, arg)
  flag = [flag]
  cmd = CmdNode(cmd, flag)
  print(cmd)

