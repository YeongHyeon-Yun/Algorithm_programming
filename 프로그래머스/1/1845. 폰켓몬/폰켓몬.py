def solution(nums):
    answer = 0
    
    num_len = len(set(nums))
    result = int(len(nums)/2)
    
    answer = min(num_len, result)
    
    return answer