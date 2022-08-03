# 백준 5543번 : 상근날드

burger = []
drink = []

for _ in range(3):
  price = int(input())
  burger.append(price)

for _ in range(2):
  price = int(input())
  drink.append(price)

print(min(burger) + min(drink) - 50)