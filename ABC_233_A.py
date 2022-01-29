import math
num = input().split()

default_amount = int(num[0])
target_amount  = int(num[1])

if default_amount >= target_amount:
  print(0)
else:
  diff = target_amount - default_amount
  required_stamp = diff / 10
  print(math.ceil(required_stamp))
