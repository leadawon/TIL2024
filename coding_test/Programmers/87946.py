from itertools import permutations as pm

def solution(k, dungeons):
    answer = -1
    for maxi in range(len(dungeons),0,-1):
        cands = pm(dungeons,maxi)
        temp = []
        
        
        
        for temp in cands:
            user=k
            for te in temp:
                if user >= te[0]:
                    user-=te[1]
                else:
                    break
            else:
                return maxi
    answer = 0
    return answer