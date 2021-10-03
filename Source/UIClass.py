from typing import Optional
# TODO: add type hinting
class UI:
  def __init__(self):
    # Public vars
    input_stream: Optional[str] = None
    output_stream: optional[str] = None

  def run(self):
    input_stream: str = input("> ")

    print(self.output_stream)

