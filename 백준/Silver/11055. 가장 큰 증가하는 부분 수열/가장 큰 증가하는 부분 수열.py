import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

dp_list = [1]*n
dp_list[0] = n_list[0]

for i in range(1, n): # 현재 값
    for j in range(i): # 앞의 값
        if n_list[j] < n_list[i]:
            dp_list[i] = max(dp_list[i], dp_list[j]+n_list[i])
        else:
            dp_list[i] = max(dp_list[i], n_list[i])
            
print(max(dp_list))