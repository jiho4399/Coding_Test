# 백준 17219번 : 비밀번호 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pw = dict()

for _ in range(n):
  info = input().split()
  pw[info[0]] = info[1]

for i in range(m):
  q = input().rstrip()
  print(pw[q])