# 실패(근데 왜 안되는지 모르겠음)
h, m = map(int, input().split())
p = int(input())

rm = m+p

while rm >= 60:
    h += 1
    rm = rm-60

if h >= 24:
  h -= 24

print(h, rm)

#####################

#성공
h, m = map(int, input().split())
time = int(input())

h += time // 60
m += time % 60

if m >= 60:
  h += 1
  m -= 60

if h >= 24:
  h -= 24

print(h, m)