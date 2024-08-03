from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dd = defaultdict(int)
    for t in tangerine:
        dd[t] += 1
    arr = []
    for key,val in dd.items():
        arr.append((key,val))
    arr = sorted(arr,key=lambda x: -x[1])
    for key,val in arr:
        if k-val<=0:
            answer+=1
            break
        else:
            answer+=1
            k-=val
    
        
        
    return answer