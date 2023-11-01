n = int(input())
if n == 0:
    print(0)
else:
    # 입력받은 수를 -2로 나눈것의 나머지를 기록 
    # 나머지는 각 자리수에 해당함 
    # 몫이 0이 될 때까지 반복
    ans = ''
    while n:
        ans += str(n % 2)
        n //= 2
        n *= -1
    print(ans[::-1]) # 결과를 뒤집에서 출력 