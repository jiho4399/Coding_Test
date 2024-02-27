'''
1. 빨리 끝나는 순서대로 정렬
2. 빨리 시작하는 순서대로 정렬 
- 회의 시간을 튜플로 받고 리스트에 추가 
'''
import sys

input = sys.stdin.readline
N = int(input())
times = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x:(x[1], x[0]))

answer = 1
end_time = times[0][1]

for start, end in times[1:]:
    if end_time <= start:
        answer += 1
        end_time = end

print(answer)