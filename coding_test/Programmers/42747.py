def solution(citations):
    answer = 0
    arr = sorted(citations, reverse=True)
    for i in range(len(arr)):
        if arr[i] <= i+1:
            answer = max(arr[i],answer)
            
        elif answer < i+1:
            answer = max(i+1,answer)
        else:
            break
            
        
    
    return answer