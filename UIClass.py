from ArgParser.ArgParseClass import ArgParser
 
class UI:
  def __init__(self):
    # Public vars
    input_stream = None
    output_stream = None

    # Private vars:
    _parser = ArgParser()#TODO: Add needed Arguements


  def run(self)
    input_stream = input("> ")

    print(self.output_stream)
    return self._parser(input_stream)

