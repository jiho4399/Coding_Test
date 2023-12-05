import sys
input = sys.stdin.readline

n = int(input())
dp = [m for m in range(n+1)]

# dp[5] = dp[5-4]+1
# 새로운 제곱수가 나타나면 해당 '해당 제곱수 + 1'로 초기화 되는 규칙
for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i: # i가 5일 때 j=2 까지만 돌아감!
            break
        elif dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j] + 1
            
print(dp[n])