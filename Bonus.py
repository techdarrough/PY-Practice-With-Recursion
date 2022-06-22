# Bonus. Write a function that when given two numbers, finds their greatest common divisor.

def gcd(x,y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y)