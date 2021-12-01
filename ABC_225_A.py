x = input()
sorted_x = sorted(x)
 
 
if sorted_x[0] == sorted_x[1] == sorted_x[2]:
  print(1)
elif sorted_x[0] == sorted_x[1] or sorted_x[1] == sorted_x[2]:
  print(3)
else:
  print(6)
