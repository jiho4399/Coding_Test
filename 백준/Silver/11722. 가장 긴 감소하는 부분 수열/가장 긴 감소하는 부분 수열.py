import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

dp_list = [1]*n

# "감소"하는 부분수열이므로 
# 현재 값 보다 앞의 값이 더 크면 
# (앞의 수에 해당하는 dp_list 값 + 1)과 현재 dp_list 값을 비교하여
# 더 큰 값을 현재 위치의 dp_list에 업데이트

for i in range(n): # 현재 값
    for j in range(0, i): # 앞의 값
        if n_list[i] < n_list[j]:
            dp_list[i] = max(dp_list[i], dp_list[j]+1) 
            
print(max(dp_list))