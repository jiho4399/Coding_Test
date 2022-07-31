# 백준 2845번 : 파티가 끝나고 난 뒤

L, P = map(int, input().split())
news = list(map(int, input().split()))

for i in news:
  print(i - L * P, end=' ')