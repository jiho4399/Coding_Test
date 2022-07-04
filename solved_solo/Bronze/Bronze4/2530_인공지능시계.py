# 2530번 : 인공지능 시계
a, b, c = map(int, input().split())
d = int(input())

c += d
b += c//60
a += b//60

c %= 60
b %= 60
a %= 24

print(a, b, c)