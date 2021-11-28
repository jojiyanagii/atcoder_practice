S1 = input().split()
S2 = input().split()
S1_0= S1[0][0]
S1_1= S1[0][1]
S2_0= S2[0][0]
S2_1= S2[0][1]
 
 
if S1_0 == "." and S2_1 == "." or S1_1 == "." and S2_0 == ".":
  print("No")
else:
  print("Yes")
