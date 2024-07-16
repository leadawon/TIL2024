def solution(A,B):
    answer = 0

    first = sorted(A)
    second = sorted(B,reverse=True)
    
    for i in range(len(first)):
        answer += first[i]*second[i]
        

    return answer