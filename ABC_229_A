S, T, X = map(int, input().split())

if S < T: #日付を跨がない場合
  if S <= X < T:
    print("Yes")
  else:
    print("No")
else: #日付を跨ぐ場合
  term1 = [S, 24]
  term2 = [0, T]
  if term1[0] <= X < term1[1] or term2[0] <= X < term2[1]:
    print("Yes")
  else:
    print("No")
