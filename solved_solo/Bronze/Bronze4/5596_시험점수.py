# 백준 5596번 : 시험 점수

S = sum(map(int, input().split()))
T = sum(map(int, input().split()))

if S == T:
  print(S)
else:
  print(max(S, T))