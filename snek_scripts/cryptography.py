alphabet = list('abcdefghijklmnopqrstuvwxyz')

def ceasar_encode(string,shift):
  newstring = ''
  for x in list(string.lower()):
    if x != ' ':
      newstring = newstring + alphabet[(alphabet.index(x) + shift) % 25]
    else:
      newstring = newstring + x
  return newstring

def ceasar_decode(string,shift):
  newstring = ''
  for x in list(string.lower()):
    if x != ' ':
      newstring = newstring + alphabet[(alphabet.index(x) + (25-shift)) % 25]
    else:
      newstring = newstring + x
  return newstring

def ma_encode(string,cipher_alphabet):
  c_alphabet = list(cipher_alphabet.lower())
  new_string = ''
  for x in list(string.lower()):
    if x != ' ':
      new_string = new_string + c_alphabet[alphabet.index(x)]
    else:
      new_string = new_string + x
  return new_string

def ma_decode(string,cipher_alphabet):
  new_string = ''
  for x in list(string.lower()):
    if x != ' ':
      new_string = new_string + alphabet[list(cipher_alphabet.lower()).index(x)]
    else:
      new_string = new_string + x
  return new_string

def freq_analyze(string):
  freq_list = []
  for x in alphabet:
    freq_list.append(string.count(x))
  return freq_list