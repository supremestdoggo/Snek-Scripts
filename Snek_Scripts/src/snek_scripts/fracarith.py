def gcd(numberA, numberB):
    if (numberB == 0):
        return numberA
    else:
        return gcd(numberB, numberA % numberB)

def lcm(num,num0):
  return (abs(num*num0))//(gcd(num,num0))

class fraction:
  def __init__(self,numerator,denominator):
    try:
      self.numerator = numerator / gcd(numerator,denominator)
      self.denominator = denominator / gcd(numerator,denominator)
    except ValueError:
      print("ValueError: Numerator and denominator must be integers.")
  def __add__(self,o):
    return (self.numerator*self.denominator / lcm(self.denominator,o.denominator))+(o.numerator*o.denominator / lcm(self.denominator,o.denominator)), lcm(self.denominator,o.denominator)
  def __sub__(self,o):
    return (self.numerator*self.denominator / lcm(self.denominator,o.denominator))-(o.numerator*o.denominator / lcm(self.denominator,o.denominator)), lcm(self.denominator,o.denominator)
  def __mul__(self,o):
    return self.numerator*o.numerator, self.denominator*o.denominator
  def __truediv__(self,o):
    return self.numerator*o.denominator,self.denominator*o.numerator
  def __int__(self):
    return self.numerator / self.denominator
  def __str__(self):
    return str(self.numerator) + "/" + str(self.denominator)
  def __eq__(self,o):
    if self.numerator == o.numerator & self.denominator == o.denominator:
      return True
    else:
      return False
  def __gt__(self,o):
    if int(self - o) > 0:
      return True
    else:
      return False
  def __lt__(self,o):
    if int(self-o) < 0:
      return True
    else:
      return False