n = int(input())
dp = [1] * 10

# 길이가 1 늘어날 때 맨 뒷자리의 경우가 (0 ~ 9)에 따라 
# 같은 길이일 때 전의 경우의수 + 전의 길이일 때 같은 경우의수 규칙
for i in range(1, n) : # 길이
    for j in range(1, 10) : # 
        dp[j] += dp[j-1]

print(sum(dp) % 10007)