import sys

n = int(sys.stdin.readline())
lst = [list(sys.stdin.readline().split()) for _ in range(n)]

# 정렬기준 설정을 위해 key & lambda 사용, - 붙으면 내림차순
lst.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in lst:
    print(str(name[0]))
