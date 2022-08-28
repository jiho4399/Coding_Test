# 백준 2083번 :  럭비 클럽

name, age, weight = map(str, input().split())

while name != '#':
  if int(age) > 17 or int(weight) >= 80:
    print(name, 'Senior')
  
  else:
    print(name, 'Junior')

  name, age, weight = map(str, input().split())