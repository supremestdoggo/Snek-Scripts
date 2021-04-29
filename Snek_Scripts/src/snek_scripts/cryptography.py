alphabet = list('abcdefghijklmnopqrstuvwxyz')

def ceasar_encode(string,shift):
  newstring = ''
  for x in list(string.lower()):
    if x != ' ':
      newstring = newstring + (alphabet.index(x) + shift) % 25
    else:
      newstring = newstring + x
  return newstring

def ceasar_decode(string,shift):
  newstring = ''
  for x in list(string.lower()):
    if x != ' ':
      newstring = newstring + (alphabet.index(x) + (25-shift)) % 25
    else:
      newstring = newstring + x
  return newstring

def ma_encode(string,c_alphabet):
  cipher_alphabet = list(c_alphabet.lower())
  new_string = ''
  for x in list(string.lower()):
    if x != ' ':
      new_string = new_string + cipher_alphabet[alphabet.index(x)]
    else:
      new_string = new_string + x
  return new_string

def ma_decode(string,c_alphabet):
  cipher_alphabet = list(alphabet.lower())
  new_string = ''
  for x in list(string.lower()):
    if x != ' ':
      new_string = new_string + alphabet(cipher_alphabet.index(x))
    else:
      new_string = new_string + x
  return new_string

def freq_analyze(string):
  freq_list = []
  for x in alphabet:
    freq_list.append(string.count(x))
  return freq_list