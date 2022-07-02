lst = list(map(int, input().split()))

dice = set(lst)

if len(dice) == 1:
  price = 10000 + max(dice) * 1000

elif len(dice) == 2:
  price = 1000 + (sum(lst) - sum(dice)) * 100

else:
  price = max(dice) * 100

print(price)