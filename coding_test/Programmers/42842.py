from math import sqrt
def solution(brown, yellow):
    answer = []
    cases = []
    for i in range(1,int(sqrt(yellow+1))+1):
        if yellow%i == 0:
            cases.append(i)
    
    for sero in cases:
        garo = yellow//sero
        if brown == (garo+sero+4) * 2 - 4:
            answer = [garo+2,sero+2]
            break
    
    return answer