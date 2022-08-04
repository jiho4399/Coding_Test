# 백준 5554번 : 심부름 가는 길

time = 0

for _ in range(4):
  t = int(input())
  time += t

print(time//60)
print(time%60)