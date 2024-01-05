import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

d = [(0,1), (0,-1), (1,0), (-1,0)]
def dfs(x, y, cnt):
    graph[y][x] = 0 # 방문했을 경우 0으로 표시 
    ''' 
    상하좌우로 돌면서 연결되어 잇는 집으로 이동, 단지 수를 1 증가시켜 재귀호출
    그 값을 저장하여 반환하도록 하여 재귀호출을 해도 그 값이 유지되도록 함 
    '''
    for dx, dy in d:
        X, Y = x + dx, y + dy
        if (0 <= X < N) and (0 <= Y < N) and graph[Y][X]:
            cnt = dfs(X, Y, cnt+1)
    return cnt
          
cnt = []
''' 지도를 돌면서 집이 있을 경우 dfs를 호출하고 반환된 단지 수를 리스트에 저장 '''
for y in range(N):
    for x in range(N):
        if graph[y][x]:
            cnt.append(dfs(x, y, cnt=1))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
