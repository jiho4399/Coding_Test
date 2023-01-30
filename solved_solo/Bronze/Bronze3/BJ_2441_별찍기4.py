n = int(input())
r = n
for i in range(n):
  print(str('*'*n).rjust(r))
  n -= 1