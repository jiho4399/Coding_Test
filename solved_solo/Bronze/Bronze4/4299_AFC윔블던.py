# 백준 4299번 : AFC 윔블던

n, m = map(int, input().split())

if n-m < 0 or (n+m) % 2 != 0:
  print(-1)

else:
  a = (n+m) // 2
  b = n - a
  print(max(a, b), min(a, b))