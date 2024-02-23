'''
N의 크기에 따라 나이트가 이동할 수 있는 경우의 수가 제한
bfs 대신 그리드를 경우의 수에 따라 적용하는 방법 사용
나이트의 초기 위치는 맨 왼쪽 아래 구석이므로 세로 N의 길이에 따라 이동 패턴이 제한
'''

import sys; input = sys.stdin.readline
n, m = map(int, input().split())

if n == 1:
    print(1)
    
elif n == 2:
    print(min(4, (m+1)//2))
    
elif m <= 6:
    print(min(4, m))
    
else:
    print(m-2)