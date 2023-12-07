import sys
input = sys.stdin.readline

n = int(input())

# n 자리 수 만큼 dp 테이블 생성 
dp = [0] * (n+1)
dp[1] = 1

# 길이가 2일 경우부터 다음 차례의 경우의 수를 포함하고 있는 규칙
for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])