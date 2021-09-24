from Source.ArgParser import LexerClass, ArgParseClass
from Source import ExecuterClass

while (arg := input("file to test > ")) != "q":
  if arg == "LexerClass":
    LexerClass.test()
  if arg == "ArgParseClass":
    ArgParseClass.test()
  if arg == "ExecuterClass":
    ExecuterClass.test()
