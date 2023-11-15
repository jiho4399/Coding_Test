import sys
input = sys.stdin.readline

n = int(input())

dic = {}

for _ in range(n):
    a, b = map(str, input().split())
    dic[a] = b

dic = dict(sorted(dic.items(), reverse = True))
    
for k in dic.keys():
    if dic[k] == 'enter':
        print(k)