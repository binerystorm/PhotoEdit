if __name__ == "__main__":
  import ArgParser.ArgParseClass as a
  from UIClass import UI
else:
  from .ArgParser import ArgParseClass as a
  from .UIClass import UI

class Executer:
  def __init__(self):
    self.parser = a.ArgParser()
    self.UI = UI

  def interp(self, ast):
    func = F_TABLE[ast.val]
    
  def mainloop(self):
    self.UI.run()


if __name__ == "__main__":
  e = Executer()
  print(e.parser.parse("echo -v"))
