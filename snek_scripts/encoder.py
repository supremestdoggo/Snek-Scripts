def stoi(text):
  return int.from_bytes(text.encode('utf-8'), 'little')

def itos(number):
  return number.to_bytes((number.bit_length() + 7) // 8, 'little').decode('utf-8')