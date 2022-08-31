#  백준 1267번 : 핸드폰 요금

n = int(input())
time = list(map(int, input().split()))

fee_y = 0
fee_m = 0

for i in time:
  p, q = divmod(i, 30)
  if q != 0:
    fee_y += p*10 + 10
  else:
    fee_y += p*10 + 10

  m, k = divmod(i, 60)
  if k != 0:
    fee_m += m*15 + 15
  else:
    fee_m += m*15 + 15

if fee_y < fee_m:
  print('Y', fee_y)
elif fee_y > fee_m:
  print('M', fee_m)
else:
  print('Y M', fee_y)