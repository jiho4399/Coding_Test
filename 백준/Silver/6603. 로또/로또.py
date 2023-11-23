import sys
import itertools
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break
    lst = lst[1:]
    
    rotto = itertools.combinations(lst, 6)
    for i in rotto:
        print(*i)
    print()