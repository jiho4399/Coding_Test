def solution(s):
    s_dict = {}
    answer = []
    
    for i, ss in enumerate(s):
        if ss not in s_dict:
            answer.append(-1)
        else:
            answer.append(i - s_dict[ss])
            
        s_dict[ss] = i
    
    return answer