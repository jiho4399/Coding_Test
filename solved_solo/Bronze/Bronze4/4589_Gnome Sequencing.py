#  백준 4589번 : Gnome Sequencing
n = int(input())

print('Gnomes:')

for _ in range(n):
  lengths = list(map(int, input().split()))
  if lengths == sorted(lengths) or lengths == sorted(lengths, reverse = True):
    print('Ordered')
  else:
    print('Unordered')