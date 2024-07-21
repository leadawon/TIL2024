from collections import defaultdict

def geteles(num):
    tgs = [2,3,5,7]
    dfdict=defaultdict(int)
    for tg in tgs:
        while num%tg==0:
            num = num//tg
            dfdict[tg] += 1
    if num==1:
        return dfdict
    else:
        dfdict[num]+=1
        return dfdict
    


def solution(arr):
    answer = 0
    darr = [0 for _ in range(100)]
    for val in arr:
        eles = geteles(val)
        for k,v in eles.items():
            darr[k] = max(darr[k],v)
    answer = 1
    for i in range(1,100):
        answer *= i ** darr[i]
            
    
    return answer