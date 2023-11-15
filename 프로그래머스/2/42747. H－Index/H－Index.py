# def solution(citations):
#     # print(citations)
#     citations.sort(reverse=True)
#     # print(citations)
#     answer = 0
    
#     for i in range(len(citations)):
#         if(citations[i] < i+1):
#             answer = i
#             return answer
        
#     return len(citations)

def solution(citations):
    citations.sort(reverse=True)
    # # a = map(min, enumerate(citations, start=1))
    # a = enumerate(citations, start=1)
    # print(a)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer