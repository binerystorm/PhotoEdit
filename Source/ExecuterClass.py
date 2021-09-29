# TODO: add type hinting

if __name__ == "__main__":
  import ArgParser.ArgParseClass as a
  from UIClass import UI
else:
  from .ArgParser import ArgParseClass as a
  from .UIClass import UI

# TODO: actualy implement foto editing 
# TODO: make better I/O system(also for UIClass)
# function procedures
def echo_func(args):
  print(" ".join(args))

# flag procedures

def eq_flag(args):
  if len(args) != 2:
    return "eq flag takes two args not {}".format(len(args))
  else:
    left, right = args
    return str(left.val == right.val)

def v_flag(args):
  str_ls = []
  if len(args) == 0:
    return str(None)
  else:
    for arg in args:
      str_ls.append(str(arg))
    return " ".join(str_ls)

# function table

F_TABLE = {
    "echo": echo_func,
    }

# flag table

FL_TABLE = {
    "eq": eq_flag,
    "v": v_flag}

class Executer:
  def __init__(self):
    self.parser = a.ArgParser()
    self.UI = UI()

  # TODO: refactor (it is not a very good systema)
  def exe(self, cmd):
    root_ast = self.parser.parse(cmd)
    self.interp(root_ast)
    
  def interp(self, ast):
    global F_TABLE
    global FL_TABLE
    args = []
    func = F_TABLE[ast.val]
    for flag in ast.args:
      args.append(FL_TABLE[flag.val.strip("-")](flag.args))
    func(args)
    
  def mainloop(self):
    self.UI.run()

def test():
  e = Executer()
  while (cmd := input(">")) != "q":
    e.exe(cmd)

if __name__ == "__main__":
  test()
