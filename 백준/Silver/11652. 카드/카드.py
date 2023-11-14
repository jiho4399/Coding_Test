import sys
input = sys.stdin.readline
n = int(input())
dct = {}

for _ in range(n):
    a = int(input())
    if a not in dct:
        dct[a] = 1
    else:
        dct[a] += 1

# value 내림차순, key 오름차순
dct = sorted(dct.items(), key = lambda x: (-x[1], x[0]))
        
print(dct[0][0])

    