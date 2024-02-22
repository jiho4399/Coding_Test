'''
3의 배수임을 알기 위한 공식
해당 수의 모든 자릿수의 합이 3의 배수가 되면 된다.
또, 30의 배수이므로 숫자 내 0이 없다면 -1을 출력해야 한다. 
'''

lst = sorted(list(map(int, input())), reverse = True)

if 0 not in lst:
    print(-1)
    
else:
    if sum(lst)%3 != 0:
        print(-1)
        
    else:
        print(''.join(map(str, lst)))