def solution(citations):
    # print(citations)
    citations.sort(reverse=True)
    # print(citations)
    answer = 0
    
    for i in range(len(citations)):
        if(citations[i] < i+1):
            answer = i
            return answer
        
    return len(citations)