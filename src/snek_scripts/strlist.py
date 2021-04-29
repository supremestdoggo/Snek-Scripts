from encoder import *

def decode(intlist):
  return [itos(int(x)) for x in intlist.split(",")]

def encode(strlist):
  return ",".join([str(stoi(x)) for x in strlist])