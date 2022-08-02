# 백준 4696번 : St.Ives

n = float(input())

while n != 0:
  answer = 0
  for i in range(5):
    answer += n**i
  print('{:.2f}'.format(round(answer, 2)))

  n = float(input())