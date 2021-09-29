# TODO: add type hinting
class UI:
  def __init__(self):
    # Public vars
    input_stream = None
    output_stream = None

  def run(self):
    input_stream = input("> ")

    print(self.output_stream)
    return self._parser.parse(input_stream)

