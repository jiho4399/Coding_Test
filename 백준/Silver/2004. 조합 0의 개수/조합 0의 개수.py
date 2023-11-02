# n!의 5 개수 세는 함수
def five_count(i):
    answer = 0
    while i != 0:
        i = i // 5
        answer += i
    return answer

# n!의 2 개수 세는 함수
def two_count(i):
    answer = 0
    while i != 0:
        i = i // 2
        answer += i
    return answer


n, m = map(int, input().split())

cnt_two = two_count(n)-two_count(m)-two_count(n-m)
cnt_five = five_count(n)-five_count(m)-five_count(n-m)

if m == 0:
    print(0)
    
else:       
    print(min(cnt_two, cnt_five))