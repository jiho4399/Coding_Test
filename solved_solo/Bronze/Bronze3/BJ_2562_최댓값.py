dic = {}
for i in range(1, 10):
  n = int(input())
  dic[n] = i

print(max(dic))
print(dic[max(dic)])