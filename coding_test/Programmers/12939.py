def solution(s):
    answer = ''
    arr = list(map(int,s.split()))
    answer = f"{min(arr)} {max(arr)}"
        
    
    return answer