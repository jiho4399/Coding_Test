# 완전탐색 
move_to = int(input())
ans = abs(100 - move_to) # ++ or -- 로 이동할 경우 존재 -> 최댓값
M = int(input())

if M: # 고장난게 있을 경우만 인풋을 받음
    broken = set(input().split())
else:
    broken = set()

# 작은수에서 큰수로 이동할 때는 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올 수 있으므로 1,000,000 까지 확인!
for n in range(1000001): 
    for N in str(n):
        if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(n)) + abs(n - move_to))

print(ans)