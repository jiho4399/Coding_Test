n = int(input())
m = int(input())

answer = []
for i in range(3):
  answer.append(n*int(str(m)[i]))

for j in reversed(answer):
  print(j)

print(answer[0]*100+answer[1]*10+answer[2])