def solution(n):
    answer = 0
    for i in range(1,n+1):
        temp = 0
        start = i
        while temp < n:
            temp+= start
            start += 1
            if temp==n:
                answer+=1
    return answer