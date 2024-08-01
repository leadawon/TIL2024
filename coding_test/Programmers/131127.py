from collections import defaultdict

def check(tgdict):
    for i,v in tgdict.items():
        if v>0:
            return False
    else:
        return True

def solution(want, number, discount):
    answer = 0
    fd = defaultdict(int)
    for w,n in zip(want,number):
        fd[w] = n
    
    for i in range(10):
        fd[discount[i]] -= 1
    idx = 10
    if check(fd):
        answer+=1
    while len(discount) > idx:
        fd[discount[idx-10]] += 1
        fd[discount[idx]] -= 1
        if check(fd):
            answer+=1
        
        idx+=1
        
        
        
    return answer