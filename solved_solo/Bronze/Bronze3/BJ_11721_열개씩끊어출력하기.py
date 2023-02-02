N = str(input())

for i in range(0, len(N)//10+2):
  print(N[i*10:(i+1)*10])