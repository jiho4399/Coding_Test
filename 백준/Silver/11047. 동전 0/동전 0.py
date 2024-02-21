n, k = map(int, input().split())
money = []
answer = 0

for i in range(n):
    coin = int(input())
    if coin <= k:
        money.append(coin)

for i in money[::-1]:
    answer += k//i
    k = k%i
    
print(answer)