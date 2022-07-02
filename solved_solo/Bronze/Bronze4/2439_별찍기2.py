# 별 찍기

N = int(input())

for i in range(N):
  print(('*' * (i+1)).rjust(N))