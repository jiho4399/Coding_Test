# 백준 1247번 : 부호

import sys
input = sys.stdin.readline

for _ in range(3):
  answer = 0
  n = int(input())

  for i in range(n):
    answer += int(input())

  if answer == 0:
    print(0)
  elif answer > 0:
    print('+')
  elif answer < 0:
    print('-')