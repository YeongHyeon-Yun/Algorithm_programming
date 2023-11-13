def solution(array, commands):
    
    answer = []
    
    for target in commands:
        hey = array[target[0]-1:target[1]]
        hey.sort()
        answer.append(hey[target[2]-1])
    
    return answer