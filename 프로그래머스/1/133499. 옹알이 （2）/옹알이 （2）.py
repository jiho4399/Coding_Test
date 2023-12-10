def solution(babbling):
    answer = 0
    # 말 할 수 있는 단어를 공백으로 대체하고 모두 공백으로 대체 된 경우의 수를 셀 것
    can_say = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        for j in can_say:
            if j*2 not in i: # 연속해서 같은 발음을 할 수 없으므로 연속이 아니라면 공백으로 대체
                i = i.replace(j, ' ')
        
        if i.isspace():
            answer += 1
    
    return answer
                