import sys
input = sys.stdin.readline

n = int(input())
dp_list = [0] * 1001

# 초기값
dp_list[0] = 1
dp_list[1] = 1

# 점화식 경우의 수 계산
for i in range(2, n+1):
    dp_list[i] = dp_list[i-1] + 2 * dp_list[i-2]

print(dp_list[n] % 10007)