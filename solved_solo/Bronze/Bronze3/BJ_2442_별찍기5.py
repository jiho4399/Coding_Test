n = int(input())

for i in range(1, n+1):
  answer = '*'*(2*i-1)
  b = ' ' * (n-1)
  n -= 1
  print(b + answer)