import sys
input = sys.stdin.readline

A, P = map(int, input().split())
lst = [A]

while True :
    num = 0
    for i in str(lst[-1]) :
        num += int(i)**P
    
    if num in lst :
        break
    lst.append(num)

print(lst.index(num))