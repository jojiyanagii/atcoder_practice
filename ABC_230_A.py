str_num = input()

if int(str_num) >= 42:
  num = int(str_num) + 1
  s_zero = str(num).zfill(3)
else:
  s_zero = str_num.zfill(3)

print('AGC' + s_zero)
