import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split(' ')))

# 인덱스 0번째는 합이 자기 자신이기 때문에 다음 인덱스 부터 시작
# 그리고 나서 max를 출력!
for i in range(1, n):
    lst[i] = max(lst[i], lst[i]+lst[i-1])

print(max(lst))