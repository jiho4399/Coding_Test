import sys
input = sys.stdin.readline

n = int(input())

dp_list = [0]*101
dp_list[0] = 1
dp_list[1] = 1
dp_list[2] = 1

for i in range(3, 101):
    dp_list[i] = dp_list[i-3] + dp_list[i-2]

for i in range(n):
    m = int(input())
    print(dp_list[m-1])